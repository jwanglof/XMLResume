<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.com/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<head><title>Hej</title></head>
			<body>
				<table>
					<thead>
						<tr>
							<th>Hej</th>
							<th>Hejhej</th>
						</tr>
					</thead>
					<tbody>
						<xsl:apply-templates select="data/userInformation" />
					</tbody>
				</table>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="userInformation">
		<tr>
			<td>
				<xsl:value-of select="@name" />
			</td>
		</tr>
	</xsl:template>
</xsl:stylesheet>