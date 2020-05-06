from .sport_event_controller import SportEventsApi, SportEventApi


def initialize_routes(api):
    api.add_resource(SportEventsApi, '/sport-event')
    api.add_resource(SportEventApi, '/sport-event/<id>')
