import nox


@nox.session(python=["3.7", "3.8"], reuse_venv=True)
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)