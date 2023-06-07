# package-example

Build rpm package with command:

```
docker run -ti -v "$PWD/package-example/:/pkg" -w /pkg docker.io/rockylinux:9 bash package.sh
```

