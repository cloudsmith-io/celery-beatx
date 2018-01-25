from unittest.mock import Mock


def get_mock_app(store_url='mock://'):
    return Mock(
        conf=Mock(
            beat_schedule={},
            beat_store=store_url,
            beat_store_lock_ttl=60,

            beat_store_classes={
                'dummy': 'beatx.store.dummy.Store',
                'redis': 'beatx.store.redis.Store',
                'mock': Mock(
                    spec=type, return_value=Mock(
                        acquire_lock=Mock(return_value=True),
                        has_locked=Mock(return_value=True),
                        load_entries=Mock(return_value={}),
                    )),
                'mock+inactive': Mock(
                    spec=type, return_value=Mock(
                        acquire_lock=Mock(return_value=False),
                        has_locked=Mock(return_value=False),
                        load_entries=Mock(return_value={}),
                    ))
            }
        )
    )