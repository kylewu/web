'''
    Copyright (C) 2017 Gitcoin Core

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

from django.core.management.base import BaseCommand
from django.utils import timezone

from economy.models import ConversionRate
from gas.models import GasProfile
from marketing.models import Stat


class Command(BaseCommand):

    help = 'cleans up database objects that are old'

    def get_then(self, days_back=7):
        return timezone.now() - timezone.timedelta(days=days_back)

    def handle(self, *args, **options):

        result = GasProfile.objects.filter(
            created_on__lt=self.get_then(7),
            ).delete()
        print(f'GasProfile: {result}')

        result = ConversionRate.objects.filter(
                created_on__lt=self.get_then(7),
            ).exclude(
                from_currency='ETH',
                to_currency='USDT',
            ).exclude(
                from_currency='USDT',
                to_currency='ETH'
            ).delete()
        print(f'ConversionRate: {result}')

        result = Stat.objects.filter(
                created_on__lt=self.get_then(7),
            ).exclude(
                created_on__hour=1,
            ).delete()
        print(f'Stat: {result}')
