 This readme was created to test the github actions workflow demo. Check .github\workflows\github-actions-demo.yml for it :)

1) Since each step is executed on the same runner, you can share data from one step to another. For example, you can have a step that builds your application followed by a step that tests the application that was built.

2) You can configure a job's dependencies with other jobs; by default, jobs have no dependencies and run in parallel with each other. When a job takes a dependency on another job, it will wait for the dependent job to complete before it can run.

3) - uses: actions/checkout@v3 --> The uses keyword specifies that this step will run v3 of the actions/checkout action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will run against the repository's code.

Source: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions