<template>
  <div v-if="siteLinks[0]" class="links">
    <div class="line">
      <Icon size="20">
        <Link />
      </Icon>
      <span class="title">网站列表</span>
    </div>
    <!-- 网站列表 -->
    <Swiper
      v-if="siteLinks[0]"
      :modules="[Pagination, Mousewheel]"
      :slides-per-view="1"
      :space-between="40"
      :pagination="{
        el: '.swiper-pagination',
        clickable: true,
        bulletElement: 'div',
      }"
      :mousewheel="true"
    >
      <SwiperSlide v-for="site in siteLinksList" :key="site">
        <el-row class="link-all" :gutter="20">
          <el-col v-for="(item, index) in site" :span="8" :key="item">
            <div
              class="item cards"
              :style="index < 3 ? 'margin-bottom: 20px' : null"
              @click="jumpLink(item)"
            >
              <Icon size="26">
                <component :is="siteIcon[item.icon]" />
              </Icon>
              <span class="name text-hidden">{{ item.name }}</span>
            </div>
          </el-col>
        </el-row>
      </SwiperSlide>
      <div class="swiper-pagination" />
    </Swiper>
  </div>

  

  <div v-if="showAnnouncementA" class="web_notice" @click="closeAnnouncement('A')">
			<div class="web_notice_box">
				<h3 class="web_notice_title">! 公告/答疑 !</h3>
				<h3 class="web_notice_title2">! 点击任意位置即可关闭 !</h3>
				<h3 class="web_notice_title">!当前页面仅供参考！代码尚未优化 !</h3>
				<h3 class="web_notice_title">!当前页面仅供参考！代码尚未优化 !</h3>
				<h3 class="web_notice_title">!当前页面仅供参考！代码尚未优化 !</h3>
				<p>更新日志：
				<br><br>2024.4.26
				<br>使用imsyy大佬的模板修改（测试中）
				<br><br>2024.4.19
				<br>更新突然＊恋人全部信息；
				<br>更新制服女友steam信息；
				<br>更新“视觉小说”史低价格表数据；
				<br>更新“音声作品”全部数据
				<br><br>2024.4.3
				<br>更新板块“黑名单”首位小黑子
				<br><br>2024.4.2
				<br>修改页面样式——按键切换页面；
				<br>创建页面“视觉小说”、“音声作品”、“实物周边”、“黑名单”四大板块。
				<br><br>2024.4.1
				<br>新增主页公告与答疑弹窗；
				<br>移动样式到独立文件
				<br><br>2024.3.28
				<br>新增表格列“其他途径史低”
				<br><br>2024.3.24
				<br>创建项目</p>
				<div class="web_notice_content">
					<p class="web_notice_content_1">注：以下是近期遇到的本页相关“名词”或其他疑问的解答。</p>
					<p>问：什么是“HF促销最低价”？<br>答：“HF促销最低价”是指<a href="https://store.hikarifield.co.jp/">HIKARI FIELD</a>商城在售的视觉小说官方促销价历史最低的价格。</p>
					<p>问：什么是“代购¥”？<br>答：“代购¥”是本人代为购买相关作品的价格。<br>（注！该价格仅在促销期间有效，价格仅供参考，在网页服务正常运作的情况下实际售价绝不高于公示价。）</p>
					<p>问：什么是“抽奖链接¥”？<br>答：“抽奖链接¥”是指本人在HF积分抽奖中抽出作品的出售价。<br>（“抽奖链接¥”的前提1.该作品为HF抽奖产出的奖品，2.本人不需要该奖品）<br>注：“抽奖链接¥”非常驻出售，请关注本人🐟/贴吧相关信息。</p>
					<p>问：什么是“抽奖key¥”？<br>答：“抽奖key¥”与链接性质差不多，不过只有SteamKEY<br>（“抽奖key¥”的前提1.该作品为HF抽奖产出的奖品，2.本人需要该奖品用于激活HF账号，但不需要该作品的steam激活码）<br>注：“抽抽奖key¥”非常驻出售，请关注本人🐟/贴吧相关信息。</p>
					<p>问：待补充<br>答：待补充</p>
					<p class="web_notice_content_1">以上就是对对于本页相关内容的答疑，如果还有其他问题欢迎联系我。</p>
					<p>! 点击任意位置即可关闭 !</p>
				</div>
			</div>
		</div>

    <div v-if="showAnnouncementB" class="web_notice" @click="closeAnnouncement('B')">
			<div class="web_notice_box">
				<h3 class="web_notice_title">! 公告/答疑 !</h3>
				<h3 class="web_notice_title2">! 点击任意位置即可关闭 !</h3>
				<div id="switchTable1" class="switchTable">
          <table border="0" cellspacing="0" cellpadding="0">
				<!--标题-->
				<tr>
					<th>游戏名称<p class="top">点击名称即可访问HF商城</p></th>
					<th>HF促销最低价<p class="top">代购价格为系统计算仅供参考<br>实际代购价格低于公示价<br>且满100还有额外折扣</p>最后更新时间2024.04.19<br>代购/抽奖标价</th>
					<th>Steam历史最低价<p class="top_redfont">注意！受汇率影响</p><p class="top">换算人民币价格仅供参考<br>此处未计算Steam余额等其他折扣</p>最后更新时间2024.03.24<br>最后补充时间2024.04.19<br>区域-价格</th>
					<th>其他途径史低<p class="top">如有补充欢迎联系</p></th>
					<th>游戏ID<p class="top">Steam商品ID</p></th>
					<th>开发商<p class="top">部分社团资料较少<br>如有错误欢迎指正</p></th>
					<th>发售时间<p class="top">此处时间采集于HF游戏介绍</p></th>
				</tr>
				<!--序号1-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/tayutama2">游魂2-you're the only one-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥21</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/552280">印度 ₹212</a><br>约¥18.33</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>552280</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2016-12-09</td>
				</tr>
				<!--序号2-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/sakura_no_mori">樱之杜†净梦者</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥21</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/749520">哈萨克斯坦 780₸</a><br>约¥12.57</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>749520</td>
					<!--开发商-->
					<td><a href="https://www.moon-stone.jp/">MOONSTONE</a><br>又称“月石社”<br>原CIRCUS部分人员建立</td>
					<!--发售时间-->
					<td>2017-12-29</td>
				</tr>
				<!--序号3-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/monobeno">茂伸奇谈-Monobeno-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥21</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/758090">印度 ₹170</a><br>约¥14.70</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>758090</td>
					<!--开发商-->
					<td><a href="https://www.lose.jp/">Lose</a><br>已停止活动</td>
					<!--发售时间-->
					<td>2018-01-26</td>
				</tr>
				<!--序号4-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/monobeno_happy_end">茂伸奇谈-Happy End-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥20</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/831660">印度 ₹209</a><br>约¥18.07</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>831660</td>
					<!--开发商-->
					<td><a href="https://www.lose.jp/">Lose</a><br>已停止活动</td>
					<!--发售时间-->
					<td>2018-05-22</td>
				</tr>
				<!--序号5-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/hello_lady">淑女同萌！</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥23</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/783120">印度 ₹230</a><br>约¥19.88</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>783120</td>
					<!--开发商-->
					<td><a href="http://akatsukiworks.com/">晓WORKS</a><br>AKABEi_SOFT2旗下</td>
					<!--发售时间-->
					<td>2018-06-29</td>
				</tr>
				<!--序号6-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/maitetsu_pure_station">爱上火车-Pure Station-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥24</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/880950">印度 ₹204</a><br>约¥17.64</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>880950</td>
					<!--开发商-->
					<td><a href="https://www.lose.jp/">Lose</a><br>已停止活动</td>
					<!--发售时间-->
					<td>2018-09-21</td>
				</tr>
				<!--序号7-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/sakura_no_mori2">樱之杜†净梦者2</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥23</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/983150">印度 ₹187</a><br>约¥16.17</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>983150</td>
					<!--开发商-->
					<td><a href="https://www.moon-stone.jp/">MOONSTONE</a><br>又称“月石社”<br>原CIRCUS部分人员建立</td>
					<!--发售时间-->
					<td>2019-03-15</td>
				</tr>
				<!--序号8-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/hello_lady_nd">淑女同萌！-New Division-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥19</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1025070">哈萨克斯坦 936₸</a><br>约¥15.08</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1025070</td>
					<!--开发商-->
					<td><a href="http://akatsukiworks.com/">晓WORKS</a><br>AKABEi_SOFT2旗下</td>
					<!--发售时间-->
					<td>2019-04-19</td>
				</tr>
				<!--序号9-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/tsukikage">月影魅像-解放之羽-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥22</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1069230">哈萨克斯坦 875₸</a><br>约¥14.10</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1069230</td>
					<!--开发商-->
					<td><a href="http://www.applique-soft.com/">Applique</a><br>隶属于AKABEiSOFT2</td>
					<!--发售时间-->
					<td>2019-07-26</td>
				</tr>
				<!--序号10-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/aokana">苍之彼方的四重奏</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥40</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1044620">俄罗斯 459₽</a><br>约¥36.01</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1044620</td>
					<!--开发商-->
					<td><a href="https://sprite.net/">sprite</a><br>Rightway Co.,Ltd旗下有限公司Axcel所属</td>
					<!--发售时间-->
					<td>2019-09-28</td>
				</tr>
				<!--序号11-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/alias_carnival">爱丽娅的明日盛典！（ALIA's Carnival!）</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥24</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1094530">印度 ₹244</a><br>约¥21.09</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1094530</td>
					<!--开发商-->
					<td><a href="http://nanawind.jp/">NanaWind</a><br>Asuka Design（アスカデザイン）旗下</td>
					<!--发售时间-->
					<td>2019-11-15</td>
				</tr>
				<!--序号12-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/natsunoiro">追忆夏色年华</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥24</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1161190">印度 ₹237</a><br>约¥20.49</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1161190</td>
					<!--开发商-->
					<td><a href="https://www.moon-stone.jp/">MOONSTONE</a><br>又称“月石社”<br>原CIRCUS部分人员建立</td>
					<!--发售时间-->
					<td>2019-12-06</td>
				</tr>
				<!--序号13-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/senren_banka">千恋＊万花</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥45</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1144400">印度 ₹432</a><br>约¥37.35</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1144400</td>
					<!--开发商-->
					<td><a href="http://www.yuzu-soft.com/">YUZUSOFT</a><br>又称“柚子社”</td>
					<!--发售时间-->
					<td>2020-02-14</td>
				</tr>
				<!--序号14-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/tryment_alpha">TrymenT ―献给渴望改变的你― Alpha篇</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥23</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1183260">印度 ₹237</a><br>约¥20.49</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1183260</td>
					<!--开发商-->
					<td><a href="https://re-tryment.com/">TrymenT</a><br>一般也可将其视作RASK作品</td>
					<!--发售时间-->
					<td>2020-02-20</td>
				</tr>
				<!--序号15-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/happiness2">Happiness！2 樱花盛典</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥25</p></td>
					<!--Steam历史最低价-->
					<td>暂未在Steam发布</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>暂未在Steam发布</td>
					<!--开发商-->
					<td><a href="https://windmill.suki.jp/">Windmill Oasis</a><br>又称“风车社”<br>ARES旗下</td>
					<!--发售时间-->
					<td>2020-04-24</td>
				</tr>
				<!--序号16-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/maitetsu_lastrun">爱上火车-Last Run!!-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥35</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1434480">乌克兰 236₴</a><br>约¥43.91</td>
					<!--其他途径史低-->
					<td><p class="top"><a href="https://www.dlsite.com/pro/work/=/product_id/VJ013196.html">【官方中日双文版】爱上火车 Last Run!! ＆ Vocal Complete Album【含DLsite限定特典】</a><br>原价330JPY<br>新用户优惠320JPY<br>实付10JPY<br><a href="./dlsite_maitetsu_lastrun.pdf">点击查看订单截图</a></p></td>
					<!--游戏ID-->
					<td>1434480</td>
					<!--开发商-->
					<td><a href="https://www.lose.jp/">Lose</a><br>已停止活动</td>
					<!--发售时间-->
					<td>2020-10-30</td>
				</tr>
				<!--序号17-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/aokana_extra1">苍之彼方的四重奏 EXTRA1</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥32</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1340130">俄罗斯 359₽</a><br>约¥28.16</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1340130</td>
					<!--开发商-->
					<td><a href="https://sprite.net/">sprite</a><br>Rightway Co.,Ltd旗下有限公司Axcel所属</td>
					<!--发售时间-->
					<td>2020-11-06</td>
				</tr>
				<!--序号18-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/riddle_joker">Riddle Joker</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥45</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1277930">俄罗斯 532 ₽</a><br>约¥41.73</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1277930</td>
					<!--开发商-->
					<td><a href="http://www.yuzu-soft.com/">YUZUSOFT</a><br>又称“柚子社”</td>
					<!--发售时间-->
					<td>2020-12-18</td>
				</tr>
				<!--序号19-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/relief">Re:LieF 〜献给亲爱的你〜 Re:LanguagE</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥30</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1518770">印度 ₹333</a><br>约¥28.79</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1518770</td>
					<!--开发商-->
					<td><a href="http://rask-soft.com/">RASK</a></td>
					<!--发售时间-->
					<td>2021-02-26</td>
				</tr>
				<!--序号20-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/kinkoi">金辉恋曲四重奏</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥46</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1277940">俄罗斯 433₽</a><br>约¥33.97</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1277940</td>
					<!--开发商-->
					<td><a href="http://sagaplanets.product.co.jp/">SAGA PLANETS</a><br>曾属VISUAL ARTS旗下<br>2019年独立</td>
					<!--发售时间-->
					<td>2021-06-11</td>
				</tr>
				<!--序号21-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/parquet">PARQUET</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥30</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1662840">俄罗斯 359₽</a><br>约¥28.16</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1662840</td>
					<!--开发商-->
					<td><a href="http://www.yuzusoft-sour.com">YUZUSOFTSOUR</a><br>YUZUSOFT的全年龄下品牌</td>
					<!--发售时间-->
					<td>2021-08-27</td>
				</tr>
				<!--序号22-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/honoguraki">来自昏暗的时间尽头</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥26</p></td>
					<!--Steam历史最低价-->
					<td>暂未在Steam发布</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>暂未在Steam发布</td>
					<!--开发商-->
					<td><a href="https://www.moon-stone.jp/">MOONSTONE</a><br>又称“月石社”<br>原CIRCUS部分人员建立</td>
					<!--发售时间-->
					<td>2021-12-17</td>
				</tr>
				<!--序号23-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/hello_lady_se">淑女同萌！-Superior Entelecheia-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥37</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1751630">印度 ₹524</a><br>约¥45.31</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1751630</td>
					<!--开发商-->
					<td><a href="http://akatsukiworks.com/">晓WORKS</a><br>AKABEi_SOFT2旗下</td>
					<!--发售时间-->
					<td>2022-01-21</td>
				</tr>
				<!--序号24-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/madoki">雪境迷途遇仙踪</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥32</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1854980">印度 ₹342</a><br>约¥29.57</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1854980</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2022-02-04</td>
				</tr>
				<!--序号25-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/sekachu">在世界与世界的正中央</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥32</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1829650">印度 ₹342</a><br>约¥29.57</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1829650</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2022-02-11</td>
				</tr>
				<!--序号26-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/stella">星光咖啡馆与死神之蝶</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥54</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1829980">印度 ₹607</a><br>约¥52.48</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1829980</td>
					<!--开发商-->
					<td><a href="http://www.yuzu-soft.com/">YUZUSOFT</a><br>又称“柚子社”</td>
					<!--发售时间-->
					<td>2022-03-25</td>
				</tr>
				<!--序号27-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/hananono">五色浮影绽放于花之海洋</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥34</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1944250">印度 ₹349</a><br>约¥30.17</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1944250</td>
					<!--开发商-->
					<td><a href="http://www.applique-soft.com/">Applique</a><br>隶属于AKABEiSOFT2</td>
					<!--发售时间-->
					<td>2022-04-22</td>
				</tr>
				<!--序号28-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/magical_charming">魔卡魅恋！</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥31</p></td>
					<!--Steam历史最低价-->
					<td>暂未在Steam发布</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>暂未在Steam发布</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2022-05-20</td>
				</tr>
				<!--序号29-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/tsukiniyorisou">近月少女的礼仪</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥46</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1776970">俄罗斯 502₽ </a><br>约¥39.38</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1776970</td>
					<!--开发商-->
					<td><a href="https://project-navel.com/">Navel</a><br>原BasiL部分人员建立</td>
					<!--发售时间-->
					<td>2022-06-17</td>
				</tr>
				<!--序号30-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/kinkoigt">金辉恋曲四重奏 -Golden Time-</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥48</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/1985260">俄罗斯 495₽</a><br>约¥38.83</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>1985260</td>
					<!--开发商-->
					<td><a href="http://sagaplanets.product.co.jp/">SAGA PLANETS</a><br>曾属VISUAL ARTS旗下<br>2019年独立</td>
					<!--发售时间-->
					<td>2022-07-15</td>
				</tr>
				<!--序号31-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/yumahorome">真愿朦幻馆～在时间暂停的洋馆里追寻明天的羔羊们～</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥35</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2066360">俄罗斯 355₽</a><br>约¥27.85</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2066360</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2022-08-12</td>
				</tr>
				<!--序号32-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/cross_concerto">交汇协奏曲</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥36</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2109640">俄罗斯 366₽</a><br>约¥28.71</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2109640</td>
					<!--开发商-->
					<td><a href="http://www.applique-soft.com/">Applique</a><br>隶属于AKABEiSOFT2</td>
					<!--发售时间-->
					<td>2022-09-23</td>
				</tr>
				<!--序号33-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/soratoto">天空的蓝与白/如梭夏日</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥27</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2135500">俄罗斯 208₽</a><br>约¥16.31</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2135500</td>
					<!--开发商-->
					<td><a href="http://www.baristalab.jp/">Barista Lab</a></td>
					<!--发售时间-->
					<td>2022-11-04</td>
				</tr>
				<!--序号34-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/aonatsu">青夏轨迹</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥40</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2185770">印度 ₹440</a><br>约¥38.04</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2185770</td>
					<!--开发商-->
					<td>GIGA / <a href="https://www.entergram.co.jp/">ENTERGRAM</a></td>
					<!--发售时间-->
					<td>2022-12-02</td>
				</tr>
				<!--序号35-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/aokana_extra2">苍之彼方的四重奏 EXTRA2</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥52</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2206340">俄罗斯 660₽</a><br>约¥51.78</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2206340</td>
					<!--开发商-->
					<td><a href="https://sprite.net/">sprite</a><br>Rightway Co.,Ltd旗下有限公司Axcel所属</td>
					<!--发售时间-->
					<td>2022-12-16</td>
				</tr>
				<!--序号36-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/future_radio">未来广播与人工鸽</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥55</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2156620">中国 ¥60.84</a><br>约¥60.84</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2156620</td>
					<!--开发商-->
					<td><a href="https://laplacian.jp/">Laplacian</a></td>
					<!--发售时间-->
					<td>2023-02-17</td>
				</tr>
				<!--序号37-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/shuffle_ep2">SHUFFLE! episode2 ～被神与魔同时盯上的男人～</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥46</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2321180">南亚 $6.50</a><br>约¥46.98</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2321180</td>
					<!--开发商-->
					<td><a href="https://project-navel.com/">Navel</a><br>原BasiL部分人员建立</td>
					<!--发售时间-->
					<td>2023-03-10</td>
				</tr>
				<!--序号38-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/witch_garden">魔女的花园</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥43</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2347380">南亚 $6.71</a><br>约¥48.50</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2347380</td>
					<!--开发商-->
					<td><a href="https://windmill.suki.jp/">Windmill Oasis</a><br>又称“风车社”<br>ARES旗下</td>
					<!--发售时间-->
					<td>2099</td>
				</tr>
				<!--序号39-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/alias_carnival_flowering_sky">爱丽娅的明日盛典！Flowering Sky</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥45</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2425410">中国 ¥51.48</a><br>约¥51.48</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2425410</td>
					<!--开发商-->
					<td><a href="http://nanawind.jp/">NanaWind</a><br>Asuka Design（アスカデザイン）旗下</td>
					<!--发售时间-->
					<td>2023-06-21</td>
				</tr>
				<!--序号40-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/sothewitch">魔女的夜宴</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥58</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2458530">南亚 $8.87</a><br>约¥64.11</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2458530</td>
					<!--开发商-->
					<td><a href="http://www.yuzu-soft.com/">YUZUSOFT</a><br>又称“柚子社”</td>
					<!--发售时间-->
					<td>2023-07-21</td>
				</tr>
				<!--序号41-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/koikake">想要传达给你的爱恋</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥58</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2242710">南亚 $8.03</a><br>约¥58.04</td>
					<!--其他途径史低-->
					<td>2023.08.03摩点众筹实体激活卡30r<br>同时期🐟均价30-35r<br>众筹已于2023.10.01结束</td>
					<!--游戏ID-->
					<td>2242710</td>
					<!--开发商-->
					<td><a href="https://ustrack.amusecraft.com/">Us:track</a><br>AMUSE CRAFT公司旗下品牌</td>
					<!--发售时间-->
					<td>2023-08-04</td>
				</tr>
				<!--序号42-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/clover_days">幸运草的约定 Clover Days</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥56</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2430690">中国 ¥56.94</a><br>约¥56.94</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2430690</td>
					<!--开发商-->
					<td><a href="http://www.alcot.biz/">ALcot</a></td>
					<!--发售时间-->
					<td>2023-08-18</td>
				</tr>
				<!--序号43-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/arcana">炼爱秘仪</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥38</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2527460">南亚 $7.13</a><br>约¥51.53</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2527460</td>
					<!--开发商-->
					<td><a href="https://lumpofsugar.co.jp/">Lump of Sugar</a><br>又称“方糖社”</td>
					<!--发售时间-->
					<td>2023-09-22</td>
				</tr>
				<!--序号44-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/otomeriron">少女理论及其周边</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥54</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2567190">中国 ¥64.24</a><br>约¥64.24</td>
					<!--其他途径史低-->
					<td>2023.12.14摩点众筹实体激活卡30r<br>同时期🐟均价30-35r<br>众筹已于2024.02.11结束</td>
					<!--游戏ID-->
					<td>2567190</td>
					<!--开发商-->
					<td><a href="https://project-navel.com/">Navel</a><br>原BasiL部分人员建立</td>
					<!--发售时间-->
					<td>2023-12-15</td>
				</tr>
				<!--序号45-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/seikano">制服女友</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥51</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2673490">南亚 $7.86</a><br>约¥56.91</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2673490</td>
					<!--开发商-->
					<td><a href="https://www.entergram.co.jp/">ENTERGRAM</a></td>
					<!--发售时间-->
					<td>2024-03-08</td>
				</tr>
				<!--序号46-->
				<tr>
					<!--游戏名称-->
					<td><a href="https://store.hikarifield.co.jp/shop/making_lovers">突然＊恋人（Making＊Lovers）全高清合集版</a></td>
					<!--HF促销最低价-->
					<td><p class="hfSpecialOffer">¥66</p></td>
					<!--Steam历史最低价-->
					<td><a href="https://steamdb.info/app/2510810">南亚 $7.86</a><br>约¥56.91</td>
					<!--其他途径史低-->
					<td></td>
					<!--游戏ID-->
					<td>2510810</td>
					<!--开发商-->
					<td><a href="https://www.hook-net.jp/smee/">SMEE</a><br>于2007年成立，隶属于株式会社Robo Planning<br>作品以日常系恋爱喜剧系Gal男女主相声为主</td>
					<!--发售时间-->
					<td>2024-04-19</td>
				</tr>
			</table>
      </div>
			</div>
		</div>
  <div v-if="showAnnouncementC" class="announcement">公告C的内容</div>
</template>

<script setup>
import { Icon } from "@vicons/utils";
// 可前往 https://www.xicons.org 自行挑选并在此处引入
import { Link, Blog, CompactDisc, Cloud, Compass, Book, Fire, LaptopCode } from "@vicons/fa"; // 注意使用正确的类别
import { mainStore } from "@/store";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination, Mousewheel } from "swiper/modules";
import siteLinks from "@/assets/siteLinks.json";

const store = mainStore();

// 计算网站链接
const siteLinksList = computed(() => {
  const result = [];
  for (let i = 0; i < siteLinks.length; i += 6) {
    const subArr = siteLinks.slice(i, i + 6);
    result.push(subArr);
  }
  return result;
});

// 网站链接图标
const siteIcon = {
  Blog,
  Cloud,
  CompactDisc,
  Compass,
  Book,
  Fire,
  LaptopCode,
};

// 链接跳转
//const jumpLink = (data) => {
  //if (data.name === "音乐" && store.musicClick) {
    //if (typeof $openList === "function") $openList();
  //} else {
    //window.open(data.link, "_blank");
  //}
//};

onMounted(() => {
  console.log(siteLinks);
});

const showAnnouncementA = ref(true); // 默认显示公告A
const showAnnouncementB = ref(false); // 默认隐藏公告B
const showAnnouncementC = ref(false); // 默认隐藏公告C

const toggleAnnouncement = (announcement) => {
  if (announcement === 'A') {
    showAnnouncementA.value = !showAnnouncementA.value;
  } else if (announcement === 'B') {
    showAnnouncementB.value = !showAnnouncementB.value;
  } else if (announcement === 'C') {
    showAnnouncementC.value = !showAnnouncementC.value;
  }
};

const closeAnnouncement = (announcement) => {
  if (announcement === 'A') {
    showAnnouncementA.value = false;
  } else if (announcement === 'B') {
    showAnnouncementB.value = false;
  } else if (announcement === 'C') {
    showAnnouncementC.value = false;
  }
};

const jumpLink = (item) => {
  if (item.name === '公告') {
    toggleAnnouncement('A');
  } else if (item.name === '价格表') {
    toggleAnnouncement('B');
  } else if (item.name === '黑名单') {
    toggleAnnouncement('C');
  } else {
    window.open(item.link, "_blank");
  }
};
</script>

<style lang="scss" scoped>
.links {
  .line {
    margin: 2rem 0.25rem 1rem;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    animation: fade 0.5s;
    .title {
      margin-left: 8px;
      font-size: 1.15rem;
      text-shadow: 0 0 5px #00000050;
    }
  }
  .swiper {
    left: -10px;
    width: calc(100% + 20px);
    padding: 5px 10px 0;
    z-index: 0;
    .swiper-slide {
      height: 100%;
    }
    .swiper-pagination {
      margin-top: 12px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      :deep(.swiper-pagination-bullet) {
        background-color: #fff;
        width: 20px;
        height: 4px;
        margin: 0 4px;
        border-radius: 4px;
        opacity: 0.2;
        transition: opacity 0.3s;
        &.swiper-pagination-bullet-active {
          opacity: 1;
        }
        &:hover {
          opacity: 1;
        }
      }
    }
  }
  .link-all {
    height: 220px;
    .item {
      height: 100px;
      width: 100%;
      display: flex;
      align-items: center;
      flex-direction: row;
      justify-content: center;
      padding: 0 10px;
      animation: fade 0.5s;

      &:hover {
        transform: scale(1.02);
        background: rgb(0 0 0 / 40%);
        transition: 0.3s;
      }

      &:active {
        transform: scale(1);
      }

      .name {
        font-size: 1.1rem;
        margin-left: 8px;
      }
      @media (min-width: 720px) and (max-width: 820px) {
        .name {
          display: none;
        }
      }
      @media (max-width: 720px) {
        height: 80px;
      }
      @media (max-width: 460px) {
        flex-direction: column;
        .name {
          font-size: 1rem;
          margin-left: 0;
          margin-top: 8px;
        }
      }
    }
    @media (max-width: 720px) {
      height: 180px;
    }
  }
}

/* 弹窗代码样式开始 */
.web_notice {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    z-index: 99999;
}

.web_notice_box {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 100%;
    //background: #FFF(255, 255, 255, 0.8);
    transform: translate(-50%, -50%);
    border-radius: 40px;
    padding: 50px 40px;
    max-height: 80%; /* 设置最大高度，适应不同屏幕尺寸 */
    overflow-y: scroll; /* 添加垂直滚动 */
}

.web_notice_title {
    font-weight: bold;
    text-align: center;
    font-size: 30px;
}

.web_notice_title2 {
    font-weight: bold;
    text-align: center;
    font-size: 20px;
}

.web_notice_content {
    font-size: 16px;
    margin-top: 26px;
    line-height: 30px;
}

.web_notice_content_1 {
    color: #ff0000;
}

.web_notice_link {
    display: block;
    text-align: center;
    font-weight: bold;
    font-size: 19px;
    line-height: 60px;
    margin: 0 auto;
    margin-top: 45px;
    border-radius: 32px;
    width: 80%;
}
/* 弹窗代码样式结束 */

table{
	width: 100%; /* 表格宽度自适应 */
	table-layout: fixed; /* 列宽固定 */
	border-collapse: collapse;/*让靠在一起的单元格只显示一个边框，边框不进行叠加*/
}
	
table tr th{
	border: solid 1px #ccc;
	height: 30px;
	width: 200px;
	background-color: #eee;
	position: sticky;
	top: 0;
  z-index: 100; /* 确保标题在内容上方 */
}

table tr td{
	border: solid 1px #ccc;
	height: 30px;
	text-align: center;
}
	
table tr:hover{
	background-color: red;/*hover:鼠标移上去就会变成红色*/
}

.hfSpecialOffer {
	font-size: 20px;	/* 字体大小 */
	color: red;	/* 字体颜色 */
	padding:0px 0;	/* 内边距 */
	margin:0px 0;	/* 外边距 */
}

.hfSLAM_CARD {
	font-size: 20px;	/* 字体大小 */
	color: orange;	/* 字体颜色 */
	padding:0px 0;	/* 内边距 */
	margin:0px 0;	/* 外边距 */
}

.ownSell {
	font-size: 14px;	/* 字体大小 */
	color: #7B7D7D;	/* 字体颜色 */
	padding:0px 0;	/* 内边距 */
	margin:0px 0;	/* 外边距 */
}

.top {
	font-size: 14px;	/* 字体大小 */
	color: #7B7D7D;	/* 字体颜色 */
	padding:0px 0;	/* 内边距 */
	margin:0px 0;	/* 外边距 */
}

.top_redfont {
	font-size: 16px;	/* 字体大小 */
	color: red;	/* 字体颜色 */
	padding:0px 0;	/* 内边距 */
	margin:0px 0;	/* 外边距 */
}
</style>
