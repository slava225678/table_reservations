from datetime import datetime

from fastapi import status

from tests.constants import (COUNT_SEATS, TABLE_ID, TIME_RES_30_MIN,
                             TIME_RES_60_MIN)


def test_create_reservation_success(client):
    '''Создает столик с резервацией'''
    response = client.post("/tables/", json={
        "table_id": TABLE_ID,
        "name": "Столик №1",
        "location": "У окна",
        "seats": COUNT_SEATS
    })
    assert response.status_code == status.HTTP_200_OK
    table_id = response.json()["id"]

    reservation_time = datetime.now().replace(microsecond=0).isoformat()
    response = client.post(
        f"/reservations/?table_id={table_id}",
        json={
            "customer_name": "John Doe",
            "reservation_time": reservation_time,
            "duration_minutes": TIME_RES_60_MIN
        }
    )
    assert response.status_code == status.HTTP_200_OK, (
        f'Бронь должна создаваться корректно на уже существующий столик '
        f'В ответе ожидается status_code {status.HTTP_200_OK}, '
        f'получен {response.status_code}'
        )
    assert response.json()["customer_name"] == "John Doe"


def test_create_reservation_conflict(client):
    '''
    Проверяет попытку создать бронь.
    Одна успешно и одна на уже забронированное время
    '''
    reservation_time = datetime.now().replace(microsecond=0).isoformat()
    response = client.post("/tables/", json={
        "table_id": TABLE_ID,
        "name": "Столик №2",
        "location": "На балконе",
        "seats": COUNT_SEATS
    })
    table_id = response.json()["id"]
    response = client.post(
        f"/reservations/?table_id={table_id}",
        json={
            "customer_name": "Alice",
            "reservation_time": reservation_time,
            "duration_minutes": 1000
        }
    )
    assert response.status_code == status.HTTP_200_OK, (
        f'Бронь должна создаваться корректно на уже существующий столик '
        f'В ответе ожидается status_code {status.HTTP_200_OK}, '
        f'получен {response.status_code}'
        )

    response = client.post(
        f"/reservations/?table_id={table_id}",
        json={
            "customer_name": "Bob",
            "reservation_time": reservation_time,
            "duration_minutes": 1000
        }
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST, (
        f'Должна отсутствовать возможность создать брони на один столик, '
        'с пересечением времени бронирования. '
        f'В ответе ожидается status_code {status.HTTP_400_BAD_REQUEST}, '
        f'получен {response.status_code}'
    )
    assert response.json() == {
        'detail': 'Столик уже забронирован в указанное время.'
    }


def test_create_reservation_nonexistent_table(client):
    '''
    Проверяет возможность создания брони,
    с несуществующим ID столика
    '''
    response = client.post(
        "/reservations/?table_id=9999",
        json={
            "customer_name": "Ghost",
            "reservation_time": datetime.now().isoformat(),
            "duration_minutes": TIME_RES_30_MIN
        }
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND, (
        f'Нельзя создать бронь на несуществующий столик '
        f'В ответе ожидается status_code {status.HTTP_404_NOT_FOUND}, '
        f'получен {response.status_code}'
        )
    assert response.json() == {'detail': 'Столик не найден.'}
