from django.db.models import Q
from django.http import Http404

from queueService.api.serializers import QueueSerializer
from queueService.models import Queue


def get_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


def get_other_queues_info(queue: Queue) -> dict:
    response_data = QueueSerializer(queue).data
    other_queues = Queue.objects.filter(
        Q(datetime_created__lt=queue.datetime_created) &
        Q(case=queue.case) &
        Q(datetime_started__isnull=True)
    ).count()
    response_data["other_queues"] = other_queues

    return response_data
