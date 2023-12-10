module.exports = {
  js2svg: {
    indent: 2,
    pretty: true
  },

  plugins: [
    /* override default preset */
    {
      name: "preset-default",
      params: {
        overrides: {
          // inlineStyles: {
          //   onlyMatchedOnce: false,
          // },
          cleanupIDs: false
        }
      }
    },

    /* by name */
    // "removeXMLNS",
    // "cleanupListOfValues",
    // "reusePaths",
    // "convertStyleToAttrs",
    "sortAttrs"

    /* expanded notation */
    // {
    //   name: "removeAttrs",
    //   params: {
    //     attrs: "(fill|stroke)"
    //   }
    // }
  ]
}
