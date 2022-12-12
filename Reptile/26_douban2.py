import re

html="""
        <td valign="top">
            <div class="pl2">
              <a href="https://book.douban.com/subject/2046909/" onclick="&quot;moreurl(this,{i:'0'})&quot;" title="故事新编">
                故事新编
              </a>
            </div>
            
              <p class="pl">鲁迅 / 人民文学出版社 / 1973-12-01 / 0.31 元</p>
              <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.4</span>
                <span class="pl">(
                    34672人评价
                )</span>
              </div>
              
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">拾取古代传说，取一点因由，随意点染</span>
              </p>
        </td>
        
        <td valign="top">
            <div class="pl2">
              <a href="https://book.douban.com/subject/2035162/" onclick="&quot;moreurl(this,{i:'1'})&quot;" title="刀锋">
                刀锋
              </a>
                <br>
                <span style="font-size:12px;">The Razor's Edge</span>
            </div>
              <p class="pl">[英]毛姆 / 周煦良 / 上海译文出版社 / 2007-3 / 18.00元</p>
              <div class="star clearfix">
                  <span class="allstar45"></span>
                  <span class="rating_nums">9.0</span>
                <span class="pl">(
                    80978人评价
                )</span>
              </div>
              <p class="quote" style="margin: 10px 0; color: #666">
                  <span class="inq">一把刀的锋刃不容易越过；因此智者说得救之道是困难的</span>
              </p>
          </td>
"""
pattern=re.compile(r'<td.*?title="(.*?)".*?pl">(.*?)</p.*?td>',re.S)
r_list=pattern.findall(html)
print(r_list)