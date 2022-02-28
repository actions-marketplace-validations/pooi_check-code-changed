# `check-code-changed` - Github Composite Action

Check if there are any changed files in "target-path".

## Inputs

|Name|Description|
|---|---|
|`github-token`|`secrets.GITHUB_TOKEN` value|
|`target-path`|Prefix to find changed files|

## Outputs

|Name|Description|
|---|---|
|`changed`|'true' or 'false'|

## Example Workflow File

```yaml
jobs:
  pr-check:
    runs-on: ubuntu-18.04
    steps:
      - uses: actions/checkout@v2

      ...

      - uses: pooi/check-code-changed@1.0.0
        id: check-main-code-changed
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          target-path: test-web

      - name: check project with test
        if: steps.check-main-code-changed.outputs.changed == 'true'
        run: |
          ./gradlew clean check 
      - name: check project without test
        if: steps.check-main-code-changed.outputs.changed != 'true'
        run: |
          ./gradlew -x test-web:test clean check

      ...
```
