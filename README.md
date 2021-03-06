# chefdk Solus eopkg config

eopkg configuration file for installing ChefDK (Chef Development Kit)

This __does not__ configure `$PATH` settings like the `postinst` script
in the Debian package would. This is on purpose so the `chefdk` ruby
installation can be easily used with [`rbenv`](https://github.com/rbenv/rbenv)
and the [`rbenv-chefdk`](https://github.com/docwhat/rbenv-chefdk) plugin.

If you do not want to use / set up rbenv and you only plan on using the version
of Ruby bundled with Chef DK, you can set Chef DK to be the default Ruby
environment for the system by following
[these instructions](https://github.com/chef/chef-dk#using-chefdk-as-your-primary-development-environment).

## Building

### Using `package.yml`/solbuild

#### Build

```
# create a dir for chefdk in your packaging dir
mkdir -p ~/pkging/chefdk
cp package.yml ~/pkging/chefdk
cd ~/pkging/chefdk
echo 'include ../Makefile.common' > Makefile
make
```

### Using pspec.xml + actions.py like 3rd-party repo

Don't have solbuild setup and just want to get this packaged and installed? Use
the files in `xml_and_actions`:

#### Build/install

```
cd xml_and_actions
# build eopkg
sudo eopkg bi --ignore-safety pspec.xml
# install
sudo eopkg it chefdk*.eopkg
```
