from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from services.models import Subscription, Tariff, UserTariff, Transaction


class SubscriptionSerializer(serializers.ModelSerializer):
    logo = Base64ImageField()

    class Meta:
        model = Subscription
        fields = ('id',
                  'name',
                  'logo',
                  'description',
                  'usage_policy')


class TariffListSerializer(serializers.ModelSerializer):
    period = serializers.SerializerMethodField()
    test_period = serializers.SerializerMethodField()
    month_price = serializers.SerializerMethodField()
    logo = Base64ImageField(
        source='subscription.logo',
        read_only=True)

    class Meta:
        model = Tariff
        fields = ('id',
                  'logo',
                  'name',
                  'description',
                  'period',
                  'price',
                  'test_period',
                  'test_price',
                  'cashback',
                  'cashback_conditions',
                  'month_price',)

    def get_period(self, obj):
        return obj.get_period_display()

    def get_test_period(self, obj):
        return obj.get_test_period_display()

    def get_month_price(self, obj):
        return obj.price / obj.period


class SubscriptionTariffSerializer(serializers.ModelSerializer):
    logo = Base64ImageField()
    tariffs = TariffListSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = ('id',
                  'logo',
                  'description',
                  'tariffs')


class UserTariffSerializer(serializers.ModelSerializer):
    tariff = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserTariff
        fields = ('id',
                  'tariff',
                  'start_date',
                  'end_date',
                  'auto_renewal',
                  'is_direct')


class TransactionSerializer(serializers.ModelSerializer):
    user_tariff = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Transaction
        fields = ('id',
                  'user_tariff',
                  'date',
                  'amount',
                  'payment_status')


class TariffSerializer(serializers.ModelSerializer):
    subscription = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tariff
        fields = ('id',
                  'subscription',
                  'name',
                  'description',
                  'period',
                  'price',
                  'test_period',
                  'test_price',
                  'cashback',
                  'cashback_conditions')
