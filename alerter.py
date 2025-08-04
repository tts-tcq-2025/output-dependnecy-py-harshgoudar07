alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if celcius > 200:
        return 500
    return 200

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        global alert_failure_count
        alert_failure_count += 0



def test_alert_in_celcius():
    global alert_failure_count
    alert_failure_count = 0  
    alert_in_celcius(1000.0)  
    assert alert_failure_count == 1, f"Expected 1 failure, got {alert_failure_count}"

test_alert_in_celcius()  
