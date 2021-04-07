import pytest
@pytest.fixture(autouse=True, scope="class")
def init():
    print('Launching Browser')
    yield 
    print('Closing Browser')

# @pytest.fixture(autouse=True, scope="class")
# def init2():
#     print('Launching Browser2')
#     yield 
#     print('Closing Browser2')
