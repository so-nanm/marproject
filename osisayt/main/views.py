
from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils import timezone


MESSAGE = (
    "за последние два года у тебя было много хороший и не очень ситуаций, "
    "когда ты уходила в себя чтобы подумать,осмыслить что либо ты всегда "
    "включала данный трек, впиши его в бота( название бота есть у тебя на "
    "руках, ведь не зря ты ходила на улицу за ним ахпхаппах, постарайся "
    "хорошенько найти название, возможно придеться вспомнить Карину "
    "Рашидовну и ее знания)"
)


def timer_page(request):
    start_at = timezone.make_aware(
        datetime(2026, 11, 10, 0, 0),
        timezone.get_current_timezone(),
    )
    end_at = start_at + timedelta(days=7)
    now = timezone.now()

    is_finished = now >= end_at
    remaining_ms = max(0, int((end_at - now).total_seconds() * 1000))

    return render(request, "main/timer.html", {
        "is_finished": is_finished,
        "remaining_ms": remaining_ms,
        "message": MESSAGE,
    })
