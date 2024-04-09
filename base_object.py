import allure


class BaseObject(object):

    failure_exception = AssertionError

    @classmethod
    def set_cls_name(cls, new_cls_name):
        cls.__name__ = new_cls_name

    def fail(self, msg):
        raise self.failure_exception(msg)

    @allure.step("Verify lists are equal")
    def assert_lists_equal(self, cur_list, exp_list):
        if len(cur_list) != len(exp_list):
            self.fail(f"Current items {cur_list} does not match expected {exp_list}")
        for i in range(len(cur_list)):
            if cur_list[i] != exp_list[i]:
                self.fail(f"Current items {cur_list} does not match expected {exp_list}")
