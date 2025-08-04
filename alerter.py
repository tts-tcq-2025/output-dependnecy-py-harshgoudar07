def network_alert_stub(celcius):
    print("*******")
    print(f'ALERT: Temperature is {celcius} celcius')
    return 200  # Stub always returns success

def alert_in_celcius(fahrenheit, network_alert=network_alert_stub):
    print(network_alert)
    celcius = (fahrenheit - 32) * 5 / 9
    return_code = network_alert(celcius)
    print(return_code)
    global alert_failure_count
    if return_code != 200:
        alert_failure_count += 1  # <== BUG: Should be += 1

# test_alerts.py (or test block)
def failing_alert_stub(celcius):
    print("-----------")
    # Simulate failure for high temp
    if celcius > 200:
        return 500
    return 200

def test_alert_failure_count():
    global alert_failure_count
    alert_failure_count = 0  # Reset before test
    alert_in_celcius(400.5, failing_alert_stub)  # This should cause a failure
    alert_in_celcius(303.6, failing_alert_stub)  # This should cause a failure
    print(alert_failure_count)
    assert alert_failure_count == 2, f"Expected 2 failures, got {alert_failure_count}"

# Run the test
test_alert_failure_count()
