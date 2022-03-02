# Generated by Django 2.1.2 on 2019-01-28 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('common', '0001_initial'),
        ('contacts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('stage', models.CharField(choices=[('QUALIFICATION', 'QUALIFICATION'), ('NEEDS ANALYSIS', 'NEEDS ANALYSIS'), ('VALUE PROPOSITION', 'VALUE PROPOSITION'), ('ID.DECISION MAKERS', 'ID.DECISION MAKERS'), ('PERCEPTION ANALYSIS', 'PERCEPTION ANALYSIS'), ('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'), ('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'), ('CLOSED WON', 'CLOSED WON'), ('CLOSED LOST', 'CLOSED LOST')], max_length=64, verbose_name='Stage')),
                ('currency', models.CharField(blank=True, choices=[('AED', 'AED, Dirham'), ('AFN', 'AFN, Afghani'), ('ALL', 'ALL, Lek'), ('AMD', 'AMD, Dram'), ('ANG', 'ANG, Guilder'), ('AOA', 'AOA, Kwanza'), ('ARS', 'ARS, Peso'), ('AUD', 'AUD, Dollar'), ('AWG', 'AWG, Guilder'), ('AZN', 'AZN, Manat'), ('BAM', 'BAM, Marka'), ('BBD', 'BBD, Dollar'), ('BDT', 'BDT, Taka'), ('BGN', 'BGN, Lev'), ('BHD', 'BHD, Dinar'), ('BIF', 'BIF, Franc'), ('BMD', 'BMD, Dollar'), ('BND', 'BND, Dollar'), ('BOB', 'BOB, Boliviano'), ('BRL', 'BRL, Real'), ('BSD', 'BSD, Dollar'), ('BTN', 'BTN, Ngultrum'), ('BWP', 'BWP, Pula'), ('BYR', 'BYR, Ruble'), ('BZD', 'BZD, Dollar'), ('CAD', 'CAD, Dollar'), ('CDF', 'CDF, Franc'), ('CHF', 'CHF, Franc'), ('CLP', 'CLP, Peso'), ('CNY', 'CNY, Yuan Renminbi'), ('COP', 'COP, Peso'), ('CRC', 'CRC, Colon'), ('CUP', 'CUP, Peso'), ('CVE', 'CVE, Escudo'), ('CZK', 'CZK, Koruna'), ('DJF', 'DJF, Franc'), ('DKK', 'DKK, Krone'), ('DOP', 'DOP, Peso'), ('DZD', 'DZD, Dinar'), ('EGP', 'EGP, Pound'), ('ERN', 'ERN, Nakfa'), ('ETB', 'ETB, Birr'), ('EUR', 'EUR, Euro'), ('FJD', 'FJD, Dollar'), ('FKP', 'FKP, Pound'), ('GBP', 'GBP, Pound'), ('GEL', 'GEL, Lari'), ('GHS', 'GHS, Cedi'), ('GIP', 'GIP, Pound'), ('GMD', 'GMD, Dalasi'), ('GNF', 'GNF, Franc'), ('GTQ', 'GTQ, Quetzal'), ('GYD', 'GYD, Dollar'), ('HKD', 'HKD, Dollar'), ('HNL', 'HNL, Lempira'), ('HRK', 'HRK, Kuna'), ('HTG', 'HTG, Gourde'), ('HUF', 'HUF, Forint'), ('IDR', 'IDR, Rupiah'), ('ILS', 'ILS, Shekel'), ('INR', 'INR, Rupee'), ('IQD', 'IQD, Dinar'), ('IRR', 'IRR, Rial'), ('ISK', 'ISK, Krona'), ('JMD', 'JMD, Dollar'), ('JOD', 'JOD, Dinar'), ('JPY', 'JPY, Yen'), ('KES', 'KES, Shilling'), ('KGS', 'KGS, Som'), ('KHR', 'KHR, Riels'), ('KMF', 'KMF, Franc'), ('KPW', 'KPW, Won'), ('KRW', 'KRW, Won'), ('KWD', 'KWD, Dinar'), ('KYD', 'KYD, Dollar'), ('KZT', 'KZT, Tenge'), ('LAK', 'LAK, Kip'), ('LBP', 'LBP, Pound'), ('LKR', 'LKR, Rupee'), ('LRD', 'LRD, Dollar'), ('LSL', 'LSL, Loti'), ('LTL', 'LTL, Litas'), ('LVL', 'LVL, Lat'), ('LYD', 'LYD, Dinar'), ('MAD', 'MAD, Dirham'), ('MDL', 'MDL, Leu'), ('MGA', 'MGA, Ariary'), ('MKD', 'MKD, Denar'), ('MMK', 'MMK, Kyat'), ('MNT', 'MNT, Tugrik'), ('MOP', 'MOP, Pataca'), ('MRO', 'MRO, Ouguiya'), ('MUR', 'MUR, Rupee'), ('MVR', 'MVR, Rufiyaa'), ('MWK', 'MWK, Kwacha'), ('MXN', 'MXN, Peso'), ('MYR', 'MYR, Ringgit'), ('MZN', 'MZN, Metical'), ('NAD', 'NAD, Dollar'), ('NGN', 'NGN, Naira'), ('NIO', 'NIO, Cordoba'), ('NOK', 'NOK, Krone'), ('NPR', 'NPR, Rupee'), ('NZD', 'NZD, Dollar'), ('OMR', 'OMR, Rial'), ('PAB', 'PAB, Balboa'), ('PEN', 'PEN, Sol'), ('PGK', 'PGK, Kina'), ('PHP', 'PHP, Peso'), ('PKR', 'PKR, Rupee'), ('PLN', 'PLN, Zloty'), ('PYG', 'PYG, Guarani'), ('QAR', 'QAR, Rial'), ('RON', 'RON, Leu'), ('RSD', 'RSD, Dinar'), ('RUB', 'RUB, Ruble'), ('RWF', 'RWF, Franc'), ('SAR', 'SAR, Rial'), ('SBD', 'SBD, Dollar'), ('SCR', 'SCR, Rupee'), ('SDG', 'SDG, Pound'), ('SEK', 'SEK, Krona'), ('SGD', 'SGD, Dollar'), ('SHP', 'SHP, Pound'), ('SLL', 'SLL, Leone'), ('SOS', 'SOS, Shilling'), ('SRD', 'SRD, Dollar'), ('SSP', 'SSP, Pound'), ('STD', 'STD, Dobra'), ('SYP', 'SYP, Pound'), ('SZL', 'SZL, Lilangeni'), ('THB', 'THB, Baht'), ('TJS', 'TJS, Somoni'), ('TMT', 'TMT, Manat'), ('TND', 'TND, Dinar'), ('TOP', 'TOP, Paanga'), ('TRY', 'TRY, Lira'), ('TTD', 'TTD, Dollar'), ('TWD', 'TWD, Dollar'), ('TZS', 'TZS, Shilling'), ('UAH', 'UAH, Hryvnia'), ('UGX', 'UGX, Shilling'), ('USD', '$, Dollar'), ('UYU', 'UYU, Peso'), ('UZS', 'UZS, Som'), ('VEF', 'VEF, Bolivar'), ('VND', 'VND, Dong'), ('VUV', 'VUV, Vatu'), ('WST', 'WST, Tala'), ('XAF', 'XAF, Franc'), ('XCD', 'XCD, Dollar'), ('XOF', 'XOF, Franc'), ('XPF', 'XPF, Franc'), ('YER', 'YER, Rial'), ('ZAR', 'ZAR, Rand'), ('ZMK', 'ZMK, Kwacha'), ('ZWL', 'ZWL, Dollar')], max_length=3, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Opportunity Amount')),
                ('lead_source', models.CharField(blank=True, choices=[('NONE', 'NONE'), ('CALL', 'CALL'), ('EMAIL', ' EMAIL'), ('EXISTING CUSTOMER', 'EXISTING CUSTOMER'), ('PARTNER', 'PARTNER'), ('PUBLIC RELATIONS', 'PUBLIC RELATIONS'), ('CAMPAIGN', 'CAMPAIGN'), ('WEBSITE', 'WEBSITE'), ('OTHER', 'OTHER')], max_length=255, null=True, verbose_name='Source of Lead')),
                ('probability', models.IntegerField(blank=True, default=0, null=True)),
                ('closed_on', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('is_active', models.BooleanField(default=False)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='accounts.Account')),
                ('assigned_to', models.ManyToManyField(related_name='opportunity_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('closed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_created_by', to=settings.AUTH_USER_MODEL)),
                ('teams', models.ManyToManyField(to='common.Team')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
