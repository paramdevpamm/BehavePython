
""" Executed once per test run: Before any features and scenarios are run.
    Initialize the driver and start the session.
"""


@behave_reporter()
def before_all(context):
    context.driver = webdriver.Chrome(projectname="pythonProject", jobname="Behave")


""" Executed after each step in the scenario.
    Reports the test step.
"""


@behave_reporter(screenshot=True)
def after_step(context, step):
    pass


""" Executed after each scenario in the feature.
    Reports the scenario as a test.
"""


@behave_reporter
def after_scenario(context, scenario):
    pass


""" Executed once per test run: after all features and scenarios are run.
    Quit the driver and close the session.
"""


def after_all(context):
    context.driver.quit()