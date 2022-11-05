
html_init = """
  <!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>/* copy from https://github.com/sindresorhus/github-markdown-css/ */

    html,body{background-color: #2d2d2d;}
    
    .markdown-body {
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      line-height: 1.5;
      color: #cccccc;
      font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;
      font-size: 16px;
      line-height: 1.5;
      word-wrap: break-word;
    }
    
    .markdown-body .octicon {
      display: inline-block;
      fill: currentColor;
      vertical-align: text-bottom;
    }
    
    .markdown-body figure{margin:0;padding:0; display:table;}
    .markdown-body figure figcaption{font-size:92%; text-align:center; color:#999999;}
    
    .markdown-body .anchor {
      float: left;
      line-height: 1;
      margin-left: -20px;
      padding-right: 4px;
    }
    
    .markdown-body .anchor:focus {
      outline: none;
    }
    
    .markdown-body h1 .octicon-link,
    .markdown-body h2 .octicon-link,
    .markdown-body h3 .octicon-link,
    .markdown-body h4 .octicon-link,
    .markdown-body h5 .octicon-link,
    .markdown-body h6 .octicon-link {
      color: #66cccc;
      vertical-align: middle;
      visibility: hidden;
    }
    
    .markdown-body h1:hover .anchor,
    .markdown-body h2:hover .anchor,
    .markdown-body h3:hover .anchor,
    .markdown-body h4:hover .anchor,
    .markdown-body h5:hover .anchor,
    .markdown-body h6:hover .anchor {
      text-decoration: none;
    }
    
    .markdown-body details {
      display: block;
    }
    
    .markdown-body summary {
      display: list-item;
    }
    
    .markdown-body a {
      background-color: initial;
    }
    
    .markdown-body a:active,
    .markdown-body a:hover {
      outline-width: 0;
    }
    
    .markdown-body strong {
      font-weight: inherit;
      font-weight: bolder;
    }
    .markdown-body strong{
      color: #f99157;
    }
    .markdown-body em{
      color: #ffcc66;
    }
    
    .markdown-body h1 {
      font-size: 2em;
      margin: .67em 0;
    }
    
    .markdown-body img {
      border-style: none;
    }
    
    .markdown-body code,
    .markdown-body kbd,
    .markdown-body pre {
      font-family: monospace,monospace;
      font-size: 1em;
    }
    
    .markdown-body hr {
      box-sizing: initial;
      height: 0;
      overflow: visible;
    }
    
    .markdown-body input {
      font: inherit;
      margin: 0;
    }
    
    .markdown-body input {
      overflow: visible;
    }
    
    .markdown-body [type=checkbox] {
      box-sizing: border-box;
      padding: 0;
    }
    
    .markdown-body * {
      box-sizing: border-box;
    }
    
    .markdown-body input {
      font-family: inherit;
      font-size: inherit;
      line-height: inherit;
    }
    
    .markdown-body a {
      color: #99cc99;
      text-decoration: none;
    }
    .markdown-body mjx-container[jax="SVG"] > svg a{fill:#99cc99;stroke: #99cc99;}
    
    .markdown-body a:hover {
      text-decoration: underline;
    }
    
    .markdown-body strong {
      font-weight: 600;
    }
    
    .markdown-body hr:after,
    .markdown-body hr:before {
      display: table;
      content: "";
    }
    
    .markdown-body hr:after {
      clear: both;
    }
    
    .markdown-body table {
      border-spacing: 0;
      border-collapse: collapse;
    }
    
    .markdown-body td,
    .markdown-body th {
      padding: 0;
    }
    
    .markdown-body details summary {
      cursor: pointer;
    }
    
    .markdown-body kbd {
      display: inline-block;
      padding: 3px 5px;
      font: 12px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
      line-height: 12px;
      color: #999999;
      vertical-align: middle;
      background-color: #333333;
      border: 1px solid #494949;
      border-radius: 3px;
    }
    
    .markdown-body h1,
    .markdown-body h2,
    .markdown-body h3,
    .markdown-body h4,
    .markdown-body h5,
    .markdown-body h6 {
      margin-top: 0;
      margin-bottom: 0;
    }
    
    .markdown-body h1 {
      font-size: 32px;
    }
    
    .markdown-body h1,
    .markdown-body h2 {
      font-weight: 600;
    }
    
    .markdown-body h2 {
      font-size: 24px;
    }
    
    .markdown-body h3 {
      font-size: 20px;
    }
    
    .markdown-body h3,
    .markdown-body h4 {
      font-weight: 600;
    }
    
    .markdown-body h4 {
      font-size: 16px;
    }
    
    .markdown-body h5 {
      font-size: 14px;
    }
    
    .markdown-body h5,
    .markdown-body h6 {
      font-weight: 600;
    }
    
    .markdown-body h6 {
      font-size: 12px;
    }
    
    .markdown-body p {
      margin-top: 0;
      margin-bottom: 10px;
    }
    
    .markdown-body blockquote {
      margin: 0;
    }
    
    .markdown-body ol,
    .markdown-body ul {
      padding-left: 0;
      margin-top: 0;
      margin-bottom: 0;
    }
    
    .markdown-body ol ol,
    .markdown-body ul ol {
      list-style-type: lower-roman;
    }
    
    .markdown-body ol ol ol,
    .markdown-body ol ul ol,
    .markdown-body ul ol ol,
    .markdown-body ul ul ol {
      list-style-type: lower-alpha;
    }
    
    .markdown-body dd {
      margin-left: 0;
    }
    
    .markdown-body code,
    .markdown-body pre {
      font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;
      font-size: 12px;
    }
    
    .markdown-body pre {
      margin-top: 0;
      margin-bottom: 0;
    }
    
    .markdown-body input::-webkit-inner-spin-button,
    .markdown-body input::-webkit-outer-spin-button {
      margin: 0;
      -webkit-appearance: none;
      appearance: none;
    }
    
    .markdown-body:after,
    .markdown-body:before {
      display: table;
      content: "";
    }
    
    .markdown-body:after {
      clear: both;
    }
    
    .markdown-body>:first-child {
      margin-top: 0!important;
    }
    
    .markdown-body>:last-child {
      margin-bottom: 0!important;
    }
    
    .markdown-body a:not([href]) {
      color: inherit;
      text-decoration: none;
    }
    
    .markdown-body blockquote,
    .markdown-body details,
    .markdown-body dl,
    .markdown-body ol,
    .markdown-body p,
    .markdown-body pre,
    .markdown-body table,
    .markdown-body ul {
      margin-top: 0;
      margin-bottom: 16px;
    }
    
    .markdown-body hr {
      height: .25em;
      padding: 0;
      margin: 24px 0;
      background-color: #494949;
      border: 0;
    }
    
    .markdown-body blockquote {
      padding: 0 1em;
      color: #9b9b9b;
      border-left: .25em solid #f2777a;
    }
    
    .markdown-body blockquote>:first-child {
      margin-top: 0;
    }
    
    .markdown-body blockquote>:last-child {
      margin-bottom: 0;
    }
    
    .markdown-body h1,
    .markdown-body h2,
    .markdown-body h3,
    .markdown-body h4,
    .markdown-body h5,
    .markdown-body h6 {
      margin-top: 24px;
      margin-bottom: 16px;
      font-weight: 600;
      line-height: 1.25;
    }
    
    .markdown-body h1 {
      font-size: 2em;
    }
    
    .markdown-body h1,
    .markdown-body h2 {
      padding-bottom: .3em;
      border-bottom: 1px solid #434343;
      color: #66cccc;
    }
    
    .markdown-body h2 {
      font-size: 1.5em;
      color: #66cccc;
    }
    
    .markdown-body h3 {
      font-size: 1.25em;
      color: #66cccc;
    }
    
    .markdown-body h4 {
      font-size: 1em;
      color: #66cccc;
    }
    
    .markdown-body h5 {
      font-size: .875em;
      color: #66cccc;
    }
    
    .markdown-body h6 {
      font-size: .85em;
      color: #66cccc;
    }
    
    .markdown-body ol,
    .markdown-body ul {
      padding-left: 2em;
    }
    
    .markdown-body ol ol,
    .markdown-body ol ul,
    .markdown-body ul ol,
    .markdown-body ul ul {
      margin-top: 0;
      margin-bottom: 0;
    }
    
    .markdown-body li {
      word-wrap: break-all;
    }
    
    .markdown-body li>p {
      margin-top: 16px;
    }
    
    .markdown-body li+li {
      margin-top: .25em;
    }
    
    .markdown-body dl {
      padding: 0;
    }
    
    .markdown-body dl dt {
      padding: 0;
      margin-top: 16px;
      font-size: 1em;
      font-style: italic;
      font-weight: 600;
    }
    
    .markdown-body dl dd {
      padding: 0 16px;
      margin-bottom: 16px;
    }
    
    .markdown-body table {
      display: block;
      width: 100%;
      overflow: auto;
    }
    
    .markdown-body table th {
      font-weight: 600;
    }
    
    .markdown-body table td,
    .markdown-body table th {
      padding: 6px 13px;
      border: 1px solid #717171;
    }
    
    .markdown-body table tr {
      background-color: #2d2d2d;
      border-top: 1px solid #717171;
    }
    
    .markdown-body table th {
      background-color: #434343;
    }
    
    .markdown-body table tr:nth-child(2n) {
      background-color: #323232;
    }
    
    .markdown-body img {
      max-width: 100%;
      box-sizing: initial;
    }
    
    .markdown-body img[align=right] {
      padding-left: 20px;
    }
    
    .markdown-body img[align=left] {
      padding-right: 20px;
    }
    
    .markdown-body code {
      padding: .2em .4em;
      margin: 0;
      font-size: 85%;
      background-color: #333333;
      color: #999999;
      border-radius: 3px;
    }
    
    .markdown-body pre {
      word-wrap: normal;
    }
    
    .markdown-body pre>code {
      padding: 0;
      margin: 0;
       font-size: 100%;
      word-break: normal;
      white-space: pre;
      background: transparent;
      border: 0;
    }
    
    .markdown-body .highlight {
      margin-bottom: 16px;
    }
    
    .markdown-body .highlight pre {
      margin-bottom: 0;
      word-break: normal;
    }
    
    .markdown-body .highlight pre,
    .markdown-body pre {
      padding: 16px;
      overflow: auto;
      font-size: 85%;
      line-height: 1.45;
      background-color: #333333;
      border-radius: 3px;
    }
    
    .markdown-body pre code {
      display: inline;
      max-width: auto;
      padding: 0;
      margin: 0;
      overflow: visible;
      line-height: inherit;
      word-wrap: normal;
      background-color: initial;
      border: 0;
      color: #999999;
    }
    
    .markdown-body .task-list-item {
      list-style-type: none;
    }
    
    .markdown-body .task-list-item+.task-list-item {
      margin-top: 3px;
    }
    
    .markdown-body .task-list-item input {
      margin: 0 .2em .25em -1.6em;
      vertical-align: middle;
    }
    .markdown-body section.footnotes{
        margin-top:48px;
        border-top:solid 1px #494949;
        padding-top:0px;
    }
    
    @media (prefers-color-scheme: dark) {
      .markdown-body mark{color: #111;}
    }
    
    /* PrismJS 1.23.0
    https://prismjs.com/download.html#themes=prism&languages=markup+css+clike+javascript */
    /**
     * prism.js default theme for JavaScript, CSS and HTML
     * Based on dabblet (http://dabblet.com)
     * @author Lea Verou
     */
    
    
    code[class*="language-"],
    pre[class*="language-"] {
        color: black;
        background: none;
        font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        text-align: left;
        white-space: pre;
        word-spacing: normal;
        word-break: normal;
        word-wrap: normal;
        -moz-tab-size: 4;
        -o-tab-size: 4;
        tab-size: 4;
    
        -webkit-hyphens: none;
        -moz-hyphens: none;
        -ms-hyphens: none;
        hyphens: none;
    }
    
    @media print {
        code[class*="language-"],
        pre[class*="language-"] {
            text-shadow: none;
        }
    }
    
    /* Code blocks */
    pre[class*="language-"] {
        padding: 1em;
        margin: .5em 0;
        overflow: auto;
    }
    
    :not(pre) > code[class*="language-"],
    pre[class*="language-"] {
        background-color: #333333;
    }
    
    /* Inline code */
    :not(pre) > code[class*="language-"] {
        padding: .1em;
        border-radius: .3em;
        white-space: normal;
    }
    
    .token.comment,
    .token.prolog,
    .token.doctype,
    .token.cdata {
        color: #48be66;
    }
    
    .token.punctuation {
        color: #8b86c9;
    }
    
    .token.namespace {
        opacity: .7;
    }
    
    .token.property,
    .token.tag,
    .token.boolean,
    .token.number,
    .token.constant,
    .token.symbol,
    .token.deleted {
        color: #8b86c9;
    }
    
    .token.selector,
    .token.attr-name,
    .token.string,
    .token.char,
    .token.builtin,
    .token.inserted {
        color: #e6424b;
    }
    
    .token.operator,
    .token.entity,
    .token.url,
    .language-css .token.string,
    .style .token.string {
        color: #$$codeBlockColor$$;
    }
    
    .token.atrule,
    .token.attr-value,
    .token.keyword {
        color: #c33795;
    }
    
    .token.function,
    .token.class-name {
        color: #67878e;
    }
    
    .token.regex,
    .token.important,
    .token.variable {
        color: #d38e63;
    }
    
    .token.important,
    .token.bold {
        font-weight: bold;
    }
    .token.italic {
        font-style: italic;
    }
    
    .token.entity {
        cursor: help;
    }
    
    
    pre[class*="language-"].line-numbers {
      position: relative;
      padding-left: 3.8em;
      counter-reset: linenumber;
    }
    
    pre[class*="language-"].line-numbers > code {
      position: relative;
      white-space: inherit;
    }
    
    .line-numbers .line-numbers-rows {
      position: absolute;
      pointer-events: none;
      top: 0;
      font-size: 100%;
      left: -3.8em;
      width: 3em; /* works for line-numbers below 1000 lines */
      letter-spacing: -1px;
      border-right: 1px solid #6b6b6b;
    
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
    
    }
    
      .line-numbers-rows > span {
        display: block;
        counter-increment: linenumber;
      }
    
        .line-numbers-rows > span:before {
          content: counter(linenumber);
          color: #6b6b6b;
          display: block;
          padding-right: 0.8em;
          text-align: right;
        }
    
    
    </style><style>.mweb-charts{background:#fff;}
    body{ box-sizing: border-box;
        margin: 0 auto;
        padding: 28px}
    @media print{
        pre, code, pre code {
         overflow: visible !important;
         white-space: pre-wrap !important;       /* css-3 */
         white-space: -moz-pre-wrap !important;  /* Mozilla, since 1999 */
         white-space: -pre-wrap !important;      /* Opera 4-6 */
         white-space: -o-pre-wrap !important;    /* Opera 7 */
         word-wrap: break-word !important;       /* Internet Explorer 5.5+ */
        }
        html,body{margin:0;padding:4px;}
    }
    
    </style><script src="https://cdn.jsdelivr.net/npm/prismjs@1.24.1/prism.min.js"></script><script src="https://cdn.jsdelivr.net/npm/prismjs@1.24.1/plugins/line-numbers/prism-line-numbers.min.js"></script><script src="https://cdn.jsdelivr.net/npm/prismjs@1.24.1/plugins/autoloader/prism-autoloader.min.js"></script><script>window.MathJax = {     tex: { tags: 'ams', inlineMath: [ ['$','$'], ['\\(','\\)'] ] },     startup: {     pageReady() {       return MathJax.startup.defaultPageReady().then(function () {          window.mweb_mathjax_ready_val = 'yes';          if(window.mweb_mathjax_ready !== undefined){ mweb_mathjax_ready(); }       });     }   }};document.addEventListener('DOMContentLoaded', function(event) {    if (typeof Prism != 'undefined') {         Prism.highlightAll();     }});window.mweb_mathjax_ready_val = '';function theMWebMathJaxRenderIsReady(key){ return window.mweb_mathjax_ready_val; }</script><script>document.addEventListener('DOMContentLoaded', function(event) {window.mweb_mathjax_ready_val = 'yes';})</script></head><body><div id='markdown_content' class='markdown-body'>
  """

html_ending = """
  </div></body></html>
  """