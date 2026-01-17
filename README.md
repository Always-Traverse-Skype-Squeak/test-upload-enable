# CodSpeed Test Sample Repository

[![CodSpeed Badge](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/AvalancheHQ/francois-python-test)

---

Miam

This a sample repository to test the [CodSpeed](https://github.com/CodSpeedHQ/codspeed) application.

## 🚀 Getting started

1. [Click here to generate a repo](https://github.com/AvalancheHQ/python-test/generate). Create the repo in the `AvalancheHQ` organization and add your name at the beginning of the repository name. For example: `adrien-python-test`
1. Import the repository in your CodSpeed account, you can do so by clicking on the `Import` button in the [CodSpeed dashboard](http://localhost:3000/settings/organizations/AvalancheHQ)
1. Set the `CODSPEED_DEV_TOKEN` secret in your repository settings with your [CodSpeed Personal upload token
   ](http://localhost:3000/settings)
1. Set the `CODSPEED_DEV_UPLOAD_URL` secret in your repository settings with the [`RestApiEndpoint` CloudFormation output](https://eu-west-1.console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/outputs?filteringText=&filteringStatus=active&viewNested=true&stackId=arn%3Aaws%3Acloudformation%3Aeu-west-1%3A549267925584%3Astack%2Fdev-codspeed-APIStack%2F55ce5750-ed0c-11ed-a1ca-064ae02bf5e7)
1. Remove the commented lines at the top of the `.github/workflows/codspeed-dev.yml` file
1. Run the following commands in your terminal:
   ```bash
   git add .
   git commit -m 'feat: add CodSpeed workflow'
   git push
   # add empty commits to trigger the workflow
   for i in {1..10}; do sleep 2 && git commit --allow-empty -nm "chore: empty commit" && gp; done
   ```
1. Add a branch with a performance regression and some commits

   1. Replace the `iterative_fibonacci` function with the following code

      ```python
      # src/fibonacci.py

      def iterative_fibonacci(n: int) -> int:
          i = 0
          a, b = 0, 1
          for _ in range(n):
              a, b = b, a + b
              i += 1
          return a
      ```

   1. Run the following commands
      ```bash
      git checkout -b feat/regression
      git add .
      git commit -m 'feat: add monitoring to iterative fibonacci'
      gh pr create --fill
      for i in {1..10}; do sleep 2 && git commit --allow-empty -nm "chore: empty commit" && gp; done
      ```

1. Go back the `main` branch
   ```bash
   git checkout main
   ```
1. Add a branch with a performance improvement and some commits

   1. Replace the `iterative_fibonacci` function with the following code

      ```python
      # src/fibonacci.py

      def recursive_fibonacci(n: int) -> int:
          a, b = 0, 1
          for _ in range(n):
              a, b = b, a + b
          return a
      ```

   1. Run the following commands
      ```bash
      git checkout -b feat/improvement
      git add .
      git commit -m 'feat: improve recursive fibonacci by making it iterative'
      gh pr create --fill
      for i in {1..10}; do sleep 2 && git commit --allow-empty -nm "chore: empty commit" && gp; done
      ```
