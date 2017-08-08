class Constants(object):
    allowed_events = ('on_temperature', 'on_pressure', 'on_magnetism', 'on_location', 'on_combined_event_count', 'on_serial', 'set_detA_reading', 'set_detB_reading')
    web_socket_port = 9000
    static_content_port = 8080