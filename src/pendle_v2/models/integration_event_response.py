from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.join_exit_event import JoinExitEvent
    from ..models.swap_event import SwapEvent


T = TypeVar("T", bound="IntegrationEventResponse")


@_attrs_define
class IntegrationEventResponse:
    """
    Attributes:
        events (list[Union['JoinExitEvent', 'SwapEvent']]): List of events
    """

    events: list[Union["JoinExitEvent", "SwapEvent"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.swap_event import SwapEvent

        events = []
        for events_item_data in self.events:
            events_item: dict[str, Any]
            if isinstance(events_item_data, SwapEvent):
                events_item = events_item_data.to_dict()
            else:
                events_item = events_item_data.to_dict()

            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.join_exit_event import JoinExitEvent
        from ..models.swap_event import SwapEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:

            def _parse_events_item(data: object) -> Union["JoinExitEvent", "SwapEvent"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    events_item_type_0 = SwapEvent.from_dict(data)

                    return events_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                events_item_type_1 = JoinExitEvent.from_dict(data)

                return events_item_type_1

            events_item = _parse_events_item(events_item_data)

            events.append(events_item)

        integration_event_response = cls(
            events=events,
        )

        integration_event_response.additional_properties = d
        return integration_event_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
