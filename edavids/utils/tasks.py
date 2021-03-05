from celery.utils.log import  get_task_logger


from config import celery_app
from edavids.utils.emails import send_message

logger = get_task_logger(__name__)

@celery_app.task(name="send_message")
def send_message_task(email, message):
    """Send asychronus email from django app."""
    logger.info("Sent email")
    return send_message(email, message)