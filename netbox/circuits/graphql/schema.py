from typing import List

import strawberry
import strawberry_django
from strawberry.types import Info

from .types import *
from .filters import *
from netbox.graphql.resolvers import list_resolver


@strawberry.type(name='Query')
class CircuitsQuery:
    circuit: CircuitType = strawberry_django.field()

    @strawberry_django.field
    def circuit_list(self, info: Info, filters: CircuitFilter | None = strawberry.UNSET) -> List[CircuitType]:
        queryset = CircuitType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_termination: CircuitTerminationType = strawberry_django.field()

    @strawberry_django.field
    def circuit_termination_list(
        self, info: Info, filters: CircuitTerminationFilter | None = strawberry.UNSET
    ) -> List[CircuitTerminationType]:
        queryset = CircuitTerminationType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitTerminationType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    circuit_type: CircuitTypeType = strawberry_django.field()

    @strawberry_django.field
    def circuit_type_list(
        self, info: Info, filters: CircuitTypeFilter | None = strawberry.UNSET
    ) -> List[CircuitTypeType]:
        queryset = CircuitTypeType.__strawberry_django_definition__.model.objects.all()
        queryset = CircuitTypeType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider: ProviderType = strawberry_django.field()

    @strawberry_django.field
    def provider_list(self, info: Info, filters: ProviderFilter | None = strawberry.UNSET) -> List[ProviderType]:
        queryset = ProviderType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider_account: ProviderAccountType = strawberry_django.field()

    @strawberry_django.field
    def provider_account_list(
        self, info: Info, filters: ProviderAccountFilter | None = strawberry.UNSET
    ) -> List[ProviderAccountType]:
        queryset = ProviderAccountType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderAccountType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)

    provider_network: ProviderNetworkType = strawberry_django.field()

    @strawberry_django.field
    def provider_network_list(
        self, info: Info, filters: ProviderNetworkFilter | None = strawberry.UNSET
    ) -> List[ProviderNetworkType]:
        queryset = ProviderNetworkType.__strawberry_django_definition__.model.objects.all()
        queryset = ProviderNetworkType.get_queryset(queryset, info)
        return list_resolver(info, queryset, filters)
