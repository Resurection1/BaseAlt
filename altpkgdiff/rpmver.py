import logging

logger = logging.getLogger(__name__)

try:
    import rpm
except ImportError:
    rpm = None

_warned = False


def compare_version_release(a, b) -> int:
    global _warned

    if rpm is not None:
        return rpm.labelCompare(a, b)

    if not _warned:
        logger.warning(
            "rpm module not available, using fallback version comparison"
        )
        _warned = True

    return (a > b) - (a < b)
