from util import *
from at_scale_python_api.database import RESERVATION_DB_CONTROLLER
from at_scale_python_api.database import SYSTEM_DB_CONTROLLER


def get_dcgpuperf_reservations():
    systems = SYSTEM_DB_CONTROLLER.query(pool_id="56bb6264-95f9-4e23-b66d-958b34fea23b")
    system_ids = [system.id for system in systems]
    reservations = RESERVATION_DB_CONTROLLER.query(system_id=system_ids, date_time_start=str(timeframe_days_ago()))
    return reservations



def parse_conductor_reservation(reservation):
    title = reservation.title
    print(title)
    if title == "Huggingface test":
        print("\n\n\ngotem\n\n\n")
    start = parse(reservation.date_time_start)
    end = parse(reservation.date_time_end)
    return create_event(title, start, end)


def get_conductor_reservation_events(event_lists):
    reservations = get_dcgpuperf_reservations()
    for reservation in reservations:
        sut_name = reservation.system.system_datas.hostname_ip
        event = parse_conductor_reservation(reservation)
        event_lists_add_event(event_lists, event, sut_name)

def main():
    event_lists = []
    get_conductor_reservation_events(event_lists)

if __name__ == '__main__':
    main()

