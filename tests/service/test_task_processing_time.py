# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Processing time excludes idle gaps and unions overlapping workers."""

from openviking.service.task_processing_time import ProcessingClock


def test_processing_clock_unions_workers_and_excludes_idle_time(monkeypatch):
    now = [0.0]
    monkeypatch.setattr("openviking.service.task_processing_time.time.monotonic", lambda: now[0])
    clock = ProcessingClock()
    assert clock.seconds() is None
    now[0] = 10  # Initial queue wait.
    clock.enter("parse")
    now[0] = 12
    clock.enter("embedding")
    now[0] = 15
    clock.leave("parse")
    now[0] = 18
    clock.leave("embedding")
    assert clock.seconds() == 8
    now[0] = 40  # No worker: waiting for another queue.
    assert clock.seconds() == 8
    clock.enter("semantic")
    now[0] = 43
    assert clock.seconds() == 11
    clock.leave("semantic")
    now[0] = 100
    assert clock.seconds() == 11
