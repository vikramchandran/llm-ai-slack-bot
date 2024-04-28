from typing import List, Optional

from pydantic import BaseModel, Field, conlist


class ArbitraryDetails(BaseModel):
    """
    A key-value store for arbitrary details about a person, such as title, role, or company,
    that can be extracted from the message.
    """

    key: str = Field(
        ...,
        description="The key of the arbitrary detail, e.g., 'title', 'role', or 'company'. Must be in snake case.",
    )
    value: str = Field(
        ...,
        description="An arbitrary detail about a person, such as a title, role, or other information.",
    )


class PersonDetails(BaseModel):
    """
    Model for storing personal details extracted from messages, including optional fields for
    participation status and arbitrary details.
    """

    first_name: Optional[str] = Field(
        None,
        description="The first name of the person, available from the message header or email thread.",
    )
    last_name: Optional[str] = Field(
        None,
        description="The last name of the person, available from the message header or email thread.",
    )
    pronouns: Optional[str] = Field(
        None,
        description="Preferred pronouns, if mentioned by the person, available in email thread, or email signature.",
    )
    email_address: Optional[str] = Field(
        None,
        description="The person's email address, if available from the message header or email thread.",
    )
    phone_number: Optional[str] = Field(
        None,
        description="The person's phone number, if available from the message header or email thread.",
    )
    timezone: Optional[str] = Field(
        None,
        description="The person's timezone, explicitly expressed or indicated by location.",
    )
    participant: Optional[bool] = Field(
        None,
        description="Indicates if the person is intended to be or desired as a participant on the event being discussed and/or scheduled.",
    )
    participant_optional: Optional[bool] = Field(
        None,
        description="Indicates if the person is an optional participant on the event being discussed and/or scheduled. When participant = False, this will always be False.",
    )
    organizer: Optional[bool] = Field(
        None,
        description="Whether the person is the organizer of the event, such as an assistant, delegate, or secretary coordinating on behalf of another participant.",
    )
    arbitrary_details: Optional[conlist(ArbitraryDetails, max_length=5)] = Field(
        None,
        description="A list of arbitrary details about the person, limited to a maximum of 5 entries.",
    )


class PersonTermModel(BaseModel):
    """
    Model representing the list of persons involved or referenced in a scheduling interaction,
    excluding specific cases like Clara from claralabs.com.
    """

    persons: List[PersonDetails] = Field(
        ...,
        description=(
            "The list of persons, represented as PersonDetails, involved or referenced, excluding Clara from claralabs.com"
        ),
    )
