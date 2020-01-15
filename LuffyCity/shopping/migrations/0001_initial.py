# Generated by Django 2.2.6 on 2020-01-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='活动名称')),
                ('brief', models.TextField(blank=True, null=True, verbose_name='优惠券介绍')),
                ('coupon_type', models.SmallIntegerField(choices=[(0, '通用券'), (1, '满减券'), (2, '折扣券')], default=0, verbose_name='券类型')),
                ('money_equivalent_value', models.IntegerField(blank=True, default=0, null=True, verbose_name='等值货币')),
                ('off_percent', models.PositiveSmallIntegerField(blank=True, default=100, help_text='只针对折扣券，例7.9折，写79', null=True, verbose_name='折扣百分比')),
                ('minimum_consume', models.PositiveIntegerField(blank=True, default=0, help_text='仅在满减券时填写此字段', null=True, verbose_name='最低消费')),
                ('object_id', models.PositiveIntegerField(blank=True, help_text='可以把优惠券跟课程绑定', null=True, verbose_name='绑定课程')),
                ('open_date', models.DateField(verbose_name='优惠券领取开始时间')),
                ('close_date', models.DateField(verbose_name='优惠券领取结束时间')),
                ('valid_begin_date', models.DateField(blank=True, null=True, verbose_name='有效期开始时间')),
                ('valid_end_date', models.DateField(blank=True, null=True, verbose_name='有效结束时间')),
                ('coupon_valid_days', models.PositiveIntegerField(blank=True, help_text='自券被领时开始算起', null=True, verbose_name='优惠券有效期（天）')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=None, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '13. 优惠券生成规则记录',
                'verbose_name_plural': '13. 优惠券生成规则记录',
                'db_table': '13. 优惠券生成规则记录',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.SmallIntegerField(choices=[(0, '微信'), (1, '支付宝'), (2, '优惠码'), (3, '贝里')])),
                ('payment_number', models.CharField(blank=True, max_length=128, null=True, verbose_name='支付第3方订单号')),
                ('order_number', models.CharField(max_length=128, unique=True, verbose_name='订单号')),
                ('actual_amount', models.FloatField(verbose_name='实付金额')),
                ('status', models.SmallIntegerField(choices=[(0, '交易成功'), (1, '待支付'), (2, '退费申请中'), (3, '已退费'), (4, '主动取消'), (5, '超时取消')], verbose_name='状态')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='订单生成时间')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='付款时间')),
                ('cancel_time', models.DateTimeField(blank=True, null=True, verbose_name='订单取消时间')),
                ('account', models.ForeignKey(on_delete=None, to='Course.Account')),
            ],
            options={
                'verbose_name': '15. 订单表',
                'verbose_name_plural': '15. 订单表',
                'db_table': '15. 订单表',
            },
        ),
        migrations.CreateModel(
            name='TransactionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='金额')),
                ('balance', models.IntegerField(verbose_name='账户余额')),
                ('transaction_type', models.SmallIntegerField(choices=[(0, '收入'), (1, '支出'), (2, '退款'), (3, '提现')])),
                ('transaction_number', models.CharField(max_length=128, unique=True, verbose_name='流水号')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备忘录')),
                ('account', models.ForeignKey(on_delete=None, to='Course.Account')),
            ],
            options={
                'verbose_name': '17. 贝里交易记录',
                'verbose_name_plural': '17. 贝里交易记录',
                'db_table': '17. 贝里交易记录',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('original_price', models.FloatField(verbose_name='课程原价')),
                ('price', models.FloatField(verbose_name='折后价格')),
                ('valid_period_display', models.CharField(max_length=32, verbose_name='有效期显示')),
                ('valid_period', models.PositiveIntegerField(verbose_name='有效期(days)')),
                ('memo', models.CharField(blank=True, max_length=255, null=True, verbose_name='备忘录')),
                ('content_type', models.ForeignKey(on_delete=None, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=None, to='shopping.Order')),
            ],
            options={
                'verbose_name': '16. 订单详细',
                'verbose_name_plural': '16. 订单详细',
                'db_table': '16. 订单详细',
            },
        ),
        migrations.CreateModel(
            name='CouponRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=64, unique=True, verbose_name='用户优惠券记录的流水号')),
                ('status', models.SmallIntegerField(choices=[(0, '未使用'), (1, '已使用'), (2, '已过期')], default=0)),
                ('get_time', models.DateTimeField(help_text='用户领取时间', verbose_name='领取时间')),
                ('used_time', models.DateTimeField(blank=True, null=True, verbose_name='使用时间')),
                ('account', models.ForeignKey(on_delete=None, to='Course.Account', verbose_name='拥有者')),
                ('coupon', models.ForeignKey(on_delete=None, to='shopping.Coupon')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=None, to='shopping.Order', verbose_name='关联订单')),
            ],
            options={
                'verbose_name': '14. 用户优惠券领取使用记录表',
                'verbose_name_plural': '14. 用户优惠券领取使用记录表',
                'db_table': '14. 用户优惠券领取使用记录表',
            },
        ),
    ]
