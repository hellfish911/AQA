"""This module contains tests."""

from hw_sixteen import TeamLead


def test_team_lead_attributes():
    """Create team lead."""
    team_lead = TeamLead(
        name='John',
        salary=6,
        department='Engineering',
        programming_language='Python',
        team_size=5,
    )

    assert hasattr(team_lead, 'name'), "Attribute 'name' is missing"
    assert hasattr(team_lead, 'salary'), "Attribute 'salary' is missing"
    assert hasattr(team_lead, 'department'), (
        "Attribute 'department' is missing"
    )
    assert hasattr(team_lead, 'programming_language'), (
        "Attribute 'programming_language' is missing"
    )
    assert hasattr(team_lead, 'team_size'), "Attribute 'team_size' is missing"

    print('Tests passed')


test_team_lead_attributes()
