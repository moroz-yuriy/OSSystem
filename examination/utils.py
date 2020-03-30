from .models import Result


def get_next_question(user, topic):
    user_result = list(
        Result.objects.filter(user=user, topic=topic).values_list('question', flat=True))
    questions = list(topic.question_set.values_list('id', flat=True))

    return set(questions).difference(set(user_result))


def get_result(results):
    good = 0
    bad = 0
    for result in results:
        if result.answer.right:
            good = good + 1
        else:
            bad = bad + 1

    return {'good': good, 'bad': bad, 'percentage': int(good / len(results) * 100)}
