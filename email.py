import win32com.client

def send_email_via_outlook(html_content, subject="Exemplo - Book1 Excel"):
    """
    Envia um email em HTML usando o Outlook local.
    'html_content' deve conter a string HTML completa (com <html>...</html>).
    """
    # 1) Cria instância do Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")
    
    # 2) Cria um novo email (Item=0 => mail item)
    mail = outlook.CreateItem(0)
    
    # 3) Configura destinatário(s) e assunto
    mail.To = "destinatario@seudominio.com"
    # mail.CC = "copias@seudominio.com"   # se quiser cópia
    # mail.BCC = "oculto@seudominio.com"  # se quiser cópia oculta
    mail.Subject = subject
    
    # 4) Define o corpo como HTML
    mail.HTMLBody = html_content
    
    # 5) Opcional: anexo, se quiser
    # mail.Attachments.Add("c:\\caminho\\de\\arquivo.pdf")
    
    # 6) Envia diretamente ou apenas abre o e-mail para visualização
    # mail.Send()      # envia direto
    mail.Display()     # exibe o e-mail na tela, permitindo edição antes do envio

# -------------------------------------------------------------------
if __name__ == "__main__":
    # Aqui está o HTML adaptado em tabelas, com ícones como imagens:
    html_code = r"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Book1 - Excel (Adaptado para E-mail)</title>
</head>
<body style="margin:0; padding:0; background:#fff; font-family:'Noto Sans', sans-serif; color:#444; font-size:14px;">

<!-- Tabela externa que envolve todo o layout -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; background:#fff;">
  
  <!-- Título (Book1 - Excel) -->
  <tr>
    <td align="center" style="background:#217346; color:#fff; padding:15px;">
      <span style="font-size:18px; font-weight:bold;">Book1 - Excel</span>
    </td>
  </tr>

  <!-- Menu-bar (File, Home, Insert, ...) -->
  <tr>
    <td style="background:#f3f2f1; padding:10px 0;">
      <table border="0" cellspacing="0" cellpadding="0" align="center" style="border-collapse:collapse;">
        <tr>
          <td style="padding:0 15px;">File</td>
          <td style="padding:0 15px; border-bottom:5px solid #217346; font-weight:700;">Home</td>
          <td style="padding:0 15px;">Insert</td>
          <td style="padding:0 15px;">Page Layout</td>
          <td style="padding:0 15px;">Formulas</td>
          <td style="padding:0 15px;">Data</td>
          <td style="padding:0 15px;">Review</td>
          <td style="padding:0 15px;">View</td>
          <td style="padding:0 15px;">Help</td>
        </tr>
      </table>
    </td>
  </tr>

  <!-- Barra de ícones (Clipboard, Font, etc.) -->
  <tr>
    <td style="background:#f3f2f1; box-shadow:0 3px 5px rgba(0,0,0,0.1); padding:10px;">
      <!-- Tabela que contém os 6 blocos: Clipboard, Font, Alignment, Number, Styles, Cells -->
      <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
        <tr valign="top">
          
          <!-- 1) Clipboard -->
          <td style="border-right:1px solid #cdcdcd; padding-right:10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="2" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">
                  Clipboard
                </td>
              </tr>
              <tr>
                <!-- Ícone de Paste em destaque -->
                <td rowspan="2" align="center" style="font-size:12px;">
                  <img src="https://via.placeholder.com/30/217346/FFFFFF?text=P" alt="Paste Icon" style="display:block; margin:0 auto; width:30px; height:30px;">
                  <div style="margin-top:5px;">Paste</div>
                </td>
                <td style="font-size:12px; padding-left:8px;">
                  <img src="https://via.placeholder.com/16/cccccc/000000?text=C" alt="Cut Icon" style="vertical-align:middle; width:16px; height:16px;">
                  <span style="margin-left:5px;">Cut</span>
                </td>
              </tr>
              <tr>
                <td style="font-size:12px; padding-left:8px;">
                  <img src="https://via.placeholder.com/16/cccccc/000000?text=Co" alt="Copy Icon" style="vertical-align:middle; width:16px; height:16px;">
                  <span style="margin-left:5px;">Copy</span>
                </td>
              </tr>
            </table>
          </td>

          <!-- 2) Font -->
          <td style="border-right:1px solid #cdcdcd; padding:0 10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="4" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">Font</td>
              </tr>
              <tr>
                <!-- Seletores de Fonte e Tamanho -->
                <td style="padding-right:5px;">
                  <select style="font-size:12px;">
                    <option>Noto Sans</option>
                    <option>Arial</option>
                    <option>Calibri</option>
                  </select>
                </td>
                <td style="padding-right:5px;">
                  <select style="font-size:12px;">
                    <option>14</option>
                    <option>16</option>
                    <option>18</option>
                  </select>
                </td>
                <!-- Ícones B/I/U -->
                <td style="padding-right:5px;">
                  <img src="https://via.placeholder.com/16?text=B" alt="Bold" style="vertical-align:middle;">
                </td>
                <td>
                  <img src="https://via.placeholder.com/16?text=I" alt="Italic" style="vertical-align:middle;">
                  <img src="https://via.placeholder.com/16?text=U" alt="Underline" style="vertical-align:middle; margin-left:5px;">
                </td>
              </tr>
            </table>
          </td>

          <!-- 3) Alignment -->
          <td style="border-right:1px solid #cdcdcd; padding:0 10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="3" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">Alignment</td>
              </tr>
              <tr>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Top" alt="Align Top" style="vertical-align:middle;"><br>Top
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Mid" alt="Align Middle" style="vertical-align:middle;"><br>Middle
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Bot" alt="Align Bottom" style="vertical-align:middle;"><br>Bottom
                </td>
              </tr>
              <tr>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=L" alt="Align Left" style="vertical-align:middle;"><br>Left
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=C" alt="Align Center" style="vertical-align:middle;"><br>Center
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=R" alt="Align Right" style="vertical-align:middle;"><br>Right
                </td>
              </tr>
            </table>
          </td>

          <!-- 4) Number -->
          <td style="border-right:1px solid #cdcdcd; padding:0 10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="3" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">Number</td>
              </tr>
              <tr>
                <td colspan="3" style="padding-bottom:5px;">
                  <select style="font-size:12px;">
                    <option>General</option>
                    <option>Number</option>
                    <option>Currency</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=%25" alt="Percent" style="vertical-align:middle;"><br>% 
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=," alt="Comma" style="vertical-align:middle;"><br>, 
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=+-" alt="Inc Dec" style="vertical-align:middle;"><br>Inc/Dec
                </td>
              </tr>
            </table>
          </td>

          <!-- 5) Styles -->
          <td style="border-right:1px solid #cdcdcd; padding:0 10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="3" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">Styles</td>
              </tr>
              <tr>
                <td style="font-size:12px; text-align:center; padding:2px;">
                  <img src="https://via.placeholder.com/16?text=CF" alt="Conditional" style="vertical-align:middle;"><br>Cond
                </td>
                <td style="font-size:12px; text-align:center; padding:2px;">
                  <img src="https://via.placeholder.com/16?text=Tbl" alt="Table" style="vertical-align:middle;"><br>Table
                </td>
                <td style="font-size:12px; text-align:center; padding:2px;">
                  <img src="https://via.placeholder.com/16?text=CS" alt="Cell Styles" style="vertical-align:middle;"><br>Cell
                </td>
              </tr>
            </table>
          </td>

          <!-- 6) Cells -->
          <td style="padding:0 10px;">
            <table border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse;">
              <tr>
                <td colspan="3" style="font-size:12px; text-align:center; font-weight:bold; padding-bottom:5px;">Cells</td>
              </tr>
              <tr>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Ins" alt="Insert" style="vertical-align:middle;"><br>Insert
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Del" alt="Delete" style="vertical-align:middle;"><br>Delete
                </td>
                <td style="font-size:12px; padding:2px;" align="center">
                  <img src="https://via.placeholder.com/16?text=Fmt" alt="Format" style="vertical-align:middle;"><br>Format
                </td>
              </tr>
            </table>
          </td>

        </tr>
      </table>
    </td>
  </tr>

  <!-- "fx" area -->
  <tr>
    <td style="background:#e6e6e6; border:1px solid #e6e6e6; padding:10px;">
      <table width="100%" border="0" cellspacing="0" cellpadding="0" style="border-collapse:collapse; background:#fff;">
        <tr>
          <td width="50" style="border:1px solid #cdcdcd; text-align:center; color:#999; font-style:italic; font-weight:700; font-size:18px;">
            fx
          </td>
          <td style="border:1px solid #cdcdcd;">&nbsp;</td>
        </tr>
      </table>
    </td>
  </tr>

  <!-- "Cells" area com A,B,C... e inputs -->
  <tr>
    <td style="background:#cdcdcd; padding:5px;">
      <table border="0" cellspacing="1" cellpadding="0" style="border-collapse:collapse;">
        <!-- Linha de letras (A,B,C...) -->
        <tr>
          <td style="width:40px; background:#e6e6e6;"></td>
          <td style="width:60px; background:#e6e6e6; text-align:center;">A</td>
          <td style="width:60px; background:#e6e6e6; text-align:center;">B</td>
          <td style="width:60px; background:#e6e6e6; text-align:center;">C</td>
          <td style="width:60px; background:#e6e6e6; text-align:center;">D</td>
          <td style="width:60px; background:#e6e6e6; text-align:center;">E</td>
          <!-- etc... -->
        </tr>
        <!-- Linha 1 -->
        <tr>
          <td style="background:#e6e6e6; text-align:center;">1</td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
        </tr>
        <!-- Linha 2 -->
        <tr>
          <td style="background:#e6e6e6; text-align:center;">2</td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
          <td style="background:#fff;"><input type="text" style="border:none; width:50px;" /></td>
        </tr>
        <!-- etc... (repita para as linhas e colunas que quiser) -->
      </table>
    </td>
  </tr>

  <!-- Rodapé de links (ex: "Part of the CSS Grid Collection", etc.) -->
  <tr>
    <td style="background:#fff; padding:10px;">
      <div style="padding:6px; font-weight:bold;">
        Part of the CSS Grid Collection 👉🏻 <br>
        <a href="https://codepen.io/collection/DQvYpQ/" target="_blank">Click here!</a>
      </div>
      <div style="padding:6px; text-align:center;">
        <a href="https://twitter.com/meowlivia_" target="_blank">Twitter</a> |
        <a href="https://github.com/oliviale" target="_blank">GitHub</a> |
        <a href="https://dribbble.com/oliviale" target="_blank">Dribbble</a>
      </div>
    </td>
  </tr>

</table>
</body>
</html>"""

    # Chama a função para enviar via Outlook local
    send_email_via_outlook(html_code, subject="Layout Excel Adaptado para Email")