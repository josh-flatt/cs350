# Deployment

## About

Since our project uses Django, built through DigitalOcean, our CI/CD pipeline is fully automated.

When a commit is pushed to the repository, DigitalOcean is triggered to begin a deployment of the most recent commit.
It also has logic for success/failure of the build caked into the pipeline, but this can also be
customized to fit our needs.

## Paths

### Successful Path

When a new build starts and succeeds, the successful path pushes out the deployment of our Web Application
to the server, with the most recent build.

### Alternative Path

When a new build cannot succeed for whatever reason, like settinngs being misconfigured or other
breaking changes, our group gets notified of the failure of the build, and DigitalOcean will automatically
revert to the most recent build/deployment that succeeded without issue.
