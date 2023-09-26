import pytest
from brownie import KBaseQuestions, config, interface, network

TEST_QUESTION_TEXT = "Whats an apple?"
TEST_QUESTION_TITLE = "Apple"


def test_kbase_fulfilquestions(get_account, initial_supply, get_kbase_token, get_link_token):
    kbase_questions = KBaseQuestions.deploy(
        get_kbase_token.address, get_link_token, {'from': get_account})
    kbase_questions.fulfillQuestionAsk(
        "Qmc4z16XfHh9Bt9GWja1dVYvqKiN42gD8N4joqSN7b6W1a", "0")
    assert kbase_questions.getQuestionAsker.call(0) == get_account
    assert kbase_questions.getQuestionCID.call(
        0) == "Qmc4z16XfHh9Bt9GWja1dVYvqKiN42gD8N4joqSN7b6W1a"
    # idk
    assert kbase_questions.questions(0) == ""


def test_create_question(get_kbase_token, get_account, get_link_token):
    kbase_questions = KBaseQuestions.deploy(
        get_kbase_token.address, get_link_token, {'from': get_account})
    assert kbase_questions is not None
    interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token']).transfer(
        kbase_questions, 1000000000000000000, {'from': get_account})
    kbase_questions.createQuestion(
        TEST_QUESTION_TEXT, TEST_QUESTION_TITLE, {'from': get_account})


@pytest.fixture()
def test_kbase_answer_question(get_account, get_kbase_token, token_amount):
    kbase_questions = KBaseQuestions.deploy(
        get_kbase_token.address, {'from': get_account})
    get_kbase_token.transfer(kbase_questions.address,
                             token_amount, {'from': get_account})
    kbase_questions.fulfillQuestionAsk(
        "Qmc4z16XfHh9Bt9GWja1dVYvqKiN42gD8N4joqSN7b6W1a", "0")
    kbase_questions.fulfillAnswerQuestion(
        "Qmc2gHt642hnf27iptGbbrEG94vwGnVH48KyeMtjCF5icH", "0")
    assert kbase_questions.questionIdCounter() == 1
    assert kbase_questions.getAnswerCID(
        0, 0) == "Qmc2gHt642hnf27iptGbbrEG94vwGnVH48KyeMtjCF5icH"
    return kbase_questions


def test_kbase_accept_answer_question(get_account, get_kbase_token, token_amount, test_kbase_answer_question):
    kbase_questions = test_kbase_answer_question
    assert kbase_questions.getAnswerStatus(0, 0) is False
    kbase_questions.acceptAnswer(0, 0)
    assert kbase_questions.getAnswerStatus(0, 0) is True


def test_only_question_asker_modifier():
    pass


def test_bytes32_to_string(get_kbase_token, get_account, get_link_token):
    kbase_questions = KBaseQuestions.deploy(
        get_kbase_token.address, get_link_token, {'from': get_account})
    string = kbase_questions.bytes32ToString(
        "0x496e7472616461792028356d696e29206f70656e2c20686967682c206c6f772c")
    assert string == "Intraday (5min) open, high, low,"

    # split_up_string_in_bytes32_digestable = "Qmc2gHt642hnf2" + \
    #     "7iptGbbrEG94vwGnVH48KyeMtjCF5icH"
