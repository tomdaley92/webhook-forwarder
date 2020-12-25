# hooks-forwarder
Webhook Forwarder for Triggering CI/CD pipelines with more control. This allows us to filter requests by `git refs`.

## Configuration file
_config.yaml_

```yaml
github:

  - path: "/some/path/for/receiving/webhooks"
    secret: secret
    push:

      - url: "webhook-job/"
        key: key
        filter:
          ref: refs/heads/development

      - url: "another-webhook-job/"
        key: key
        filter:
          ref: refs/heads/stable

```

## Installing Dependencies
1. Install python3.7
2. Navigate into the project directory
3. Type `python3 -m venv venv` to create a virtual environment
4. Type `source venv/bin/activate` to activate the virtual environment
5. Type `pip install -r requirements.txt --extra-index-url https://pypi.occ.starbucks.net` to install all the pip packages

## Docker

#### Build
```bash
source build.sh
```

#### Run
```bash
source run.sh
```

#### Test
```bash
source test.sh
```

## Usage
1. Navigate into the project directory
2. Activate the virtual environment using `source venv/bin/activate`
3. Run using `python app.py`
4. Type `deactivate` when you're done, to close the virtual environment.

## Notes
- [GitHub Webhooks](https://developer.github.com/webhooks/)
- [Validating payloads](https://developer.github.com/webhooks/securing/#validating-payloads-from-github)
- [Git "Ref" Documentation](https://git-scm.com/docs/gitrevisions)
