import untable


def test_single():
    table = """<table class="infobox vcard">
        <caption class="infobox-title" style="font-size:125%; font-style:italic; padding-bottom:0.2em;">Purple Pirate
        </caption>
        <tbody>
            <tr>
                <td colspan="2" class="infobox-image"><a href="/wiki/File:Purple_pirate.jpg" class="image"><img
                            alt="Purple pirate.jpg" src="//upload.wikimedia.org/wikipedia/en/9/91/Purple_pirate.jpg"
                            decoding="async" width="200" height="295" class="thumbborder" data-file-width="200"
                            data-file-height="295"></a>
                    <div class="infobox-caption">First edition</div>
                </td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Author</th>
                <td class="infobox-data"><a href="/wiki/Talbot_Mundy" title="Talbot Mundy">Talbot Mundy</a></td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Country</th>
                <td class="infobox-data">United States</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Language</th>
                <td class="infobox-data">English</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Series</th>
                <td class="infobox-data">Tros</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Genre</th>
                <td class="infobox-data"><a href="/wiki/Fantasy_novel" class="mw-redirect" title="Fantasy novel">Fantasy
                        novel</a></td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Publisher</th>
                <td class="infobox-data"><a href="/wiki/Appleton-Century-Crofts"
                        title="Appleton-Century-Crofts">Appleton-Century</a></td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">
                    <div style="display: inline-block; line-height: 1.2em; padding: .1em 0;">Publication date</div>
                </th>
                <td class="infobox-data">1935</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Media&nbsp;type</th>
                <td class="infobox-data">Print (<a href="/wiki/Hardcover" title="Hardcover">Hardback</a>)</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Pages</th>
                <td class="infobox-data">367</td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label"><a href="/wiki/OCLC_(identifier)" class="mw-redirect"
                        title="OCLC (identifier)"><abbr title="Online Computer Library Center number">OCLC</abbr></a></th>
                <td class="infobox-data"><a rel="nofollow" class="external text"
                        href="https://www.worldcat.org/oclc/581460">581460</a></td>
            </tr>
            <tr>
                <th scope="row" class="infobox-label">Preceded&nbsp;by</th>
                <td class="infobox-data"><i>Queen Cleopatra&nbsp;</i></td>
            </tr>
        </tbody>
    </table>"""
    data = untable.single(table, skip=1)

    assert data == {
        "Author": "Talbot Mundy",
        "Country": "United States",
        "Language": "English",
        "Series": "Tros",
        "Genre": "Fantasy novel",
        "Publisher": "Appleton-Century",
        "Publication date": "1935",
        "Media type": "Print (Hardback)",
        "Pages": "367",
        "OCLC": "581460",
        "Preceded by": "Queen Cleopatra",
    }


def test_multi():
    table = """<table>
    <tr>
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
    </tr>
    <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
    </tr>
    <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
    </tr>
    </table>"""
    data = untable.multi(html=table)

    assert data == [
        {
            "Company": "Alfreds Futterkiste",
            "Contact": "Maria Anders",
            "Country": "Germany",
        },
        {
            "Company": "Centro comercial Moctezuma",
            "Contact": "Francisco Chang",
            "Country": "Mexico",
        },
    ]
