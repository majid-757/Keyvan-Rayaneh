from django.db import models
from datetime import datetime

from ckeditor.fields import RichTextField
from jalali_date import date2jalali, datetime2jalali



class CustomerRegistration(models.Model):
    class Meta:
        verbose_name = 'ثبت مشتری '
        verbose_name_plural = 'ثبت مشتری '


    firstname = models.CharField(max_length=100, verbose_name='نام')
    lastname = models.CharField(max_length=200, verbose_name='نام خانوادگی')
    landline_phone = models.CharField(max_length=100, verbose_name='تلفن ثابت', blank=True)
    mobile = models.CharField(max_length=100, verbose_name='موبایل')
    device_password = models.CharField(max_length=200, verbose_name='رمز عبور دستگاه', blank=True)
    acceptor_name = models.CharField(max_length=200, verbose_name='نام پذیرنده دستگاه')
    name_of_services = models.CharField(max_length=100, verbose_name='نام سرویس کار')
    the_name_of_the_final_tester = models.CharField(max_length=100, verbose_name='نام تستر نهایی')
    accessories = models.CharField(max_length=200, verbose_name='لوازم جانبی', blank=True)
    invoice_number = models.CharField(max_length=100, verbose_name='شماره فاکتور')
    operations_performed_on_the_device = RichTextField(verbose_name='عملیات انجام شده بر روی دستگاه')
    received_money = models.CharField(max_length=100, verbose_name='مبلغ دریافتی')
    startdatetime = models.DateTimeField(verbose_name='تاریخ و زمان', default=datetime.now)


    status_choices = (
        ("ok", "تماس گرفته شد"),
        ("off", "خاموش بود"),
        ("he_was_not_accountable", "پاسخگو نبودند"),
    )

    call_status = models.CharField(max_length=100, choices=status_choices, verbose_name="وضعیت تماس")



    def __str__(self):

        return self.firstname + " " + self.lastname



    def get_jalali_date(self):
        return datetime2jalali(self.startdatetime)







