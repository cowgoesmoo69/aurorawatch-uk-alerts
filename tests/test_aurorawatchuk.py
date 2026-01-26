from app.aurorawatchuk import process_status_ids

def test_process_status_ids_green():
    status_ids = [
        {"status_id": "green"},
        ]
    assert process_status_ids(status_ids) == 0    
    status_ids = [
        {"status_id": "green"},
        {"status_id": "green"},
        ]
    assert process_status_ids(status_ids) == 0
    status_ids = [
        {"status_id": "yellow"},
        {"status_id": "green"},
        ]
    assert process_status_ids(status_ids) == 0
    status_ids = [
        {"status_id": "amber"},
        {"status_id": "green"},
        ]
    assert process_status_ids(status_ids) == 0
    status_ids = [
        {"status_id": "red"},
        {"status_id": "green"},
        ]
    assert process_status_ids(status_ids) == 0

def test_process_status_ids_yellow():
    status_ids = [
        {"status_id": "yellow"},
        ]
    assert process_status_ids(status_ids) == 1    
    status_ids = [
        {"status_id": "yellow"},
        {"status_id": "yellow"},
        ]
    assert process_status_ids(status_ids) == 1

def test_process_status_ids_amber():
    status_ids = [
        {"status_id": "amber"},
        ]
    assert process_status_ids(status_ids) == 2    
    status_ids = [
        {"status_id": "amber"},
        {"status_id": "amber"},
        ]
    assert process_status_ids(status_ids) == 2

def test_process_status_ids_red():
    status_ids = [
        {"status_id": "red"},
        ]
    assert process_status_ids(status_ids) == 3    
    status_ids = [
        {"status_id": "red"},
        {"status_id": "red"},
        ]
    assert process_status_ids(status_ids) == 3