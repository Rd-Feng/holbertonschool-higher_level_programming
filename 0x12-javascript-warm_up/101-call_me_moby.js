#!/usr/bin/node
module.exports.callMeMoby = function (n, func) {
  for (let i = 0; i < n; i++) func()
}
