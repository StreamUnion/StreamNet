## OAuth configuration

### mysql set up

Bring mysql up

```bash
docker-compose up
```

Compile oauth services (In trias-oauth/oauth-resource/ and oauth-server/).

```bash
./gradlew clean build
```

DB migration (In trias-oauth/oauth-resource/ and oauth-server/)

```bash
./gradlew flywayClean
./gradlew flywayMigrate
```

### OAuth server / client set up

start oauth and oauth cli
```bash
export TRIAS_OAUTH_CLIENT=/opt/trias/oauth/client
mkdir -p $TRIAS_OAUTH_CLIENT
cp scripts/front_end/trias-oauth/oauth-resource/target/oauth-resource-1.0-SNAPSHOT.jar $TRIAS_OAUTH_CLIENT
cp scripts/front_end/trias-oauth/oauth-resource/src/main/resources/application.yml   $TRIAS_OAUTH_CLIENT
cp scripts/front_end/trias-oauth/oauth-resource/src/main/resources/logback-spring.xml  $TRIAS_OAUTH_CLIENT
cd $TRIAS_OAUTH_CLIENT
java -jar oauth-resource-1.0-SNAPSHOT.jar  &

export TRIAS_OAUTH_SERVER=/opt/trias/oauth/server
mkdir -p $TRIAS_OAUTH_SERVER
cp scripts/front_end/trias-oauth/oauth-server/target/oauth-server-1.0-SNAPSHOT.jar $TRIAS_OAUTH_SERVER
cp scripts/front_end/trias-oauth/oauth-server/src/main/resources/application.yml  $TRIAS_OAUTH_SERVER
cp scripts/front_end/trias-oauth/oauth-server/src/main/resources/logback-spring.xml  $TRIAS_OAUTH_SERVER
cd $TRIAS_OAUTH_SERVER
java -jar oauth-server-1.0-SNAPSHOT.jar &
```

## To start server

This document is based ontemplate for [vue-cli](https://github.com/vuejs/vue-cli)

``` bash

# modify the config
vi scripts/front_end/web/src/common/config/config.js
# Replace the ip address with the local ip address

# install dependencies
npm install

# serve with hot reload at localhost:9081
npm run dev

# build for production with minification
npm run build

```

## Folder structure
* build - webpack config files

* config - webpack config files

* dist - build

* src -your app  
  * api
  * assets
  * common
  * components - your vue components
  * mock
  * styles
  * views - your pages
  * vuex
  * App.vue
  * main.js - main file
  * routes.js

* static - static assets

## How to run in dev/product environment
### First server
- cd ~/iri/scripts/front_end/server
- go run main.go
### dev
- modify proxy file ~/config/proxyConfig.js
    - modify target with your address
- modify ~/src/common/config/config.js
    - modify the serer list you need
- npm run dev

### product
- mkdir -p /usr/share/nginx/html/trias-dag
- npm run build
- cp -r dist/* /usr/share/nginx/html/trias-dag/
        
You should use your own nginx root config  and configure the nginx.conf first.
## License
[MIT](http://opensource.org/licenses/MIT)
