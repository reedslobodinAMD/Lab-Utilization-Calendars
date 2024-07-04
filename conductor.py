from util import *
from at_scale_python_api.database import RESERVATION_DB_CONTROLLER
from at_scale_python_api.database import SYSTEM_DB_CONTROLLER


def get_dcgpuperf_reservations():
    systems = SYSTEM_DB_CONTROLLER.query(pool_id="56bb6264-95f9-4e23-b66d-958b34fea23b")
    system_ids = [system.id for system in systems] +    ["4fb54e91-5b2e-4460-b1d4-e83641bae87b", 
                                                         "0e213598-db89-4ebf-8bd3-349ed92c590e",
                                                         "37a08a93-9404-4ce8-b9eb-6e356f045756",
                                                         "60ca01b8-341c-475a-8ea4-9695ca0f7388",
                                                         "f80f4d43-6859-48e3-850e-1f7e97b70f3b",
                                                         "e9eabd0e-9587-47f0-ae26-d4ad3e18f008",
                                                         "c9ae0c32-22ce-44bc-ab5c-88d5c06d5680",
                                                         "58219c15-f20b-4473-95bc-8bdfadc8ebf4"]
    reservations = RESERVATION_DB_CONTROLLER.query(system_id=system_ids, date_time_start=str(timeframe_days_ago()))
    return reservations


'''
def parse_conductor_reservation(reservation, event_lists, sut_name):
    title = reservation.title
    #print(title)
    style = EventStyles.GREEN
    for user in reservation.users:
        team_names = [team.name for team in user.teams]
        if ("perf" not in team_names) and ("DCGPUPerf" not in team_names):
            style = EventStyles.RED
    start = utc_to_pacific(parse(reservation.date_time_start))
    end = utc_to_pacific(parse(reservation.date_time_end))
    create_event(title, start, end, event_lists, sut_name, style)
'''
def parse_reservation(event_lists, reservation):
    sut_name = reservation.system.system_datas.hostname_ip
    event_type = "dcgpuperf conductor reservation"
    for user in reservation.users:
        team_names = [team.name for team in user.teams]
        if ("perf" not in team_names) and ("DCGPUPerf" not in team_names):
            event_type = "non-dcgpuperf conductor reservation"
    event_dict = dict(Task=reservation.title,
            Start=utc_to_pacific(parse(reservation.date_time_start)),
            End=utc_to_pacific(parse(reservation.date_time_end)),
            Event_Type=event_type)
    event_lists_add(event_lists, sut_name, event_dict)
def get_conductor_reservation_events(event_lists):
    reservations = get_dcgpuperf_reservations()
    for reservation in reservations:
        parse_reservation(event_lists, reservation)

    #for reservation in reservations:
    #    sut_name = reservation.system.system_datas.hostname_ip
    #    parse_conductor_reservation(reservation, event_lists, sut_name)

def main():
    event_lists = []
    get_conductor_reservation_events(event_lists)

if __name__ == '__main__':
    main()

