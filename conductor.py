from util import *
from at_scale_python_api.database import RESERVATION_DB_CONTROLLER
from at_scale_python_api.database import SYSTEM_DB_CONTROLLER


def get_dcgpuperf_reservations():
    systems = SYSTEM_DB_CONTROLLER.query(pool_id="56bb6264-95f9-4e23-b66d-958b34fea23b")
    system_ids = [system.id for system in systems]
    reservations = RESERVATION_DB_CONTROLLER.query(system_id=system_ids, date_time_start=str(timeframe_days_ago()))
    return reservations



def parse_conductor_reservation(reservation, event_lists, sut_name):
    title = reservation.title
    print(title)
    start = utc_to_pacific(parse(reservation.date_time_start))
    end = utc_to_pacific(parse(reservation.date_time_end))
    create_event(title, start, end, event_lists, sut_name)


def get_conductor_reservation_events(event_lists):
    reservations = get_dcgpuperf_reservations()
    for reservation in reservations:
        sut_name = reservation.system.system_datas.hostname_ip
        parse_conductor_reservation(reservation, event_lists, sut_name)

def main():
    event_lists = []
    get_conductor_reservation_events(event_lists)

if __name__ == '__main__':
    main()

