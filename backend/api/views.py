from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta


from services.models import Subscription, Tariff, UserTariff, Transaction

from .serializers import (SubscriptionSerializer,
                          SubscriptionTariffSerializer,
                          TariffSerializer,
                          UserTariffSerializer)


class SubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    # для экрана choose_plan
    def retrieve(self, request, pk=None):
        subscription_id = pk
        queryset = Subscription.objects.filter(
            id=subscription_id).prefetch_related('tariffs')
        serializer = SubscriptionTariffSerializer(queryset, many=True)
        return Response(serializer.data)


class TariffViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer

    @action(methods=['post'],
            detail=True,
            url_path='subscribe')
    # метод для подписки на тариф
    def subscribe(self, request, *args, **kwargs):
        user = request.user
        tariff = self.get_object()

        # Создаем транзакцию (оплату)
        transaction_date = datetime.now().date()
        transaction = Transaction.objects.create(
            user_tariff=None,  # Пока не связываем с тарифом пользователя
            date=transaction_date,
            amount=tariff.price,
            # Имитация успешного платежа, 1 - типа тру, значит зачислено,
            # или строку можно, например, 'зачислено' или 'success'
            payment_status=1)

        start_date = transaction_date
        end_date = start_date + timedelta(days=30 * tariff.period)

        # Создаем подписку пользователя на тариф (юзер тариф)
        user_tariff = UserTariff.objects.create(
            user=user,
            tariff=tariff,
            start_date=transaction_date,
            end_date=end_date)

        # Связываем транзакцию с созданной подпиской
        transaction.user_tariff = user_tariff
        transaction.save()

        # Сериализуем и возвращаем созданную подписку
        serializer = UserTariffSerializer(user_tariff)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
