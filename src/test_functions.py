# Tests for the object in Question()
assert Question
test_question = Question("question", "answer")
assert isinstance(test_question, Question)
assert isinstance(test_question.prompt, str)
assert isinstance(test_question.answer, str)

# Test for the object in Chat
assert Chat
test_chat = Chat('Hi')