# chefdk Solus eopkg config

eopkg configuration file for installing ChefDK (Chef Development Kit)

By default __does not__ configure `$PATH` settings like the `postinst` script
in the Debian package would. This is on purpose so the `chefdk` ruby
installation can be easily used with [`rbenv`](https://github.com/rbenv/rbenv)
and the [`rbenv-chefdk`](https://github.com/docwhat/rbenv-chefdk) plugin.

## Build/install

```
./install.sh
```

Use `build.sh` if you just want to try building the eopkg yourself

### With postinst script, messes with $PATH

At your own risk, I haven't tested this at all

```
./install.sh postinst
```
