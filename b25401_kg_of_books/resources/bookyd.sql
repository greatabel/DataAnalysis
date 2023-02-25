/*
 Navicat MySQL Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50717
 Source Host           : localhost:3306
 Source Schema         : bookyd

 Target Server Type    : MySQL
 Target Server Version : 50717
 File Encoding         : 65001

 Date: 25/04/2022 18:12:27
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bookshelf
-- ----------------------------
DROP TABLE IF EXISTS `bookshelf`;
CREATE TABLE `bookshelf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bookid` int(11) DEFAULT NULL,
  `userid` int(11) DEFAULT NULL,
  `zt` int(11) DEFAULT '0' COMMENT '0,1 在读',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bookshelf
-- ----------------------------
BEGIN;
INSERT INTO `bookshelf` VALUES (2, 137, 1, 1);
INSERT INTO `bookshelf` VALUES (6, 102, 1, 1);
COMMIT;

-- ----------------------------
-- Table structure for booktb
-- ----------------------------
DROP TABLE IF EXISTS `booktb`;
CREATE TABLE `booktb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `isbn` varchar(255) DEFAULT NULL,
  `foreignability` int(11) DEFAULT '0',
  `literatureability` int(11) DEFAULT '0',
  `viewability` int(11) DEFAULT '0',
  `thinkingability` int(11) DEFAULT '0',
  `happyability` int(11) DEFAULT '0',
  `score` double(11,0) DEFAULT NULL,
  `scorenum` int(11) DEFAULT '0',
  `press` varchar(255) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `bookimg` varchar(255) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of booktb
-- ----------------------------
BEGIN;
INSERT INTO `booktb` VALUES (101, '罪与罚', ' [俄] 陀思妥耶夫斯基 / 岳麟 ', '名著', '9780864313201', 0, 2, 1, 0, 0, 9, 189, '  岳麓书社 / 2002-9 / 68.00元', '文学,计算机,', '1');
INSERT INTO `booktb` VALUES (102, '傲慢与偏见', ' [英] 奥斯丁 / 王科一 ', '名著', '9781365660801', 0, 2, 1, 0, 0, 9, 74, '  中央编译出版社 / 2013-2 / 258.00元', '文学,计算机,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (103, '圣经', ' ', '名著', '9781501749292', 0, 2, 1, 0, 0, 9, 519, '  天津社会科学出版社 / 2006-7 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (104, '论语', ' ', '名著', '9780194052610', 0, 2, 1, 0, 0, 9, 1594, '  生活·读书·新知三联 / 2006-4 / 21.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (105, '人性的枷锁', ' 威廉·萨默赛特·毛姆 / (W.S.Maugham) / 张柏然 ', '名著', '9781615641253', 0, 2, 1, 0, 0, 9, 140, '  海南出版社 / 2000-06 / 65.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (106, '围城', ' 钱钟书 ', '名著', '9781975419639', 0, 2, 1, 0, 0, 9, 65, '  商务印书馆 / 2010-01 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (107, '地下室手记', ' [俄] 陀思妥耶夫斯基 / 臧仲伦 ', '名著', '9781441328014', 0, 2, 1, 0, 0, 9, 25, '  岳麓书社 / 1994-12-01 / 680.0', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (108, '荒原狼', ' [德]赫尔曼·黑塞 / 赵登荣 / 倪诚恩 ', '名著', '9781475804447', 0, 2, 1, 0, 0, 9, 140, '  香港电影双周刊出版社 / 2005-09-12 / 138港币', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (109, '大师和玛格丽特', ' [俄] 布尔加科夫 / 钱诚 ', '名著', '9781591145332', 0, 2, 1, 0, 0, 9, 65, '  黃翠華 / 遠流出版 / 1996', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (110, '象棋的故事', ' [奥] 斯台芬·茨威格 / 张玉书 ', '名著', '9789460093326', 0, 2, 1, 0, 0, 9, 49, '  地震出版社 / 2012-7-1 / 20.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (111, '京华烟云', ' 林语堂 / 张振玉 ', '名著', '9781909487215', 0, 2, 1, 0, 0, 9, 42, ' Charles T Munger / Donning Publishing', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (112, '小王子', ' [法] 圣埃克絮佩里 / 周克希 ', '名著', '9781612191393', 0, 2, 1, 0, 0, 9, 87, '  上海译文出版社 / 2009年2月 / 45.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (113, '约翰·克里斯托夫', ' 罗曼・罗兰 / 袁俊生 汪秀华 ', '名著', '9781844155378', 0, 2, 1, 0, 0, 9, 443, '  湖南少年儿童出版社 / 1983 / 0.94', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (114, '四世同堂（上下）', ' 老舍 ', '名著', '9780702027246', 0, 2, 1, 0, 0, 9, 37, '  北京艺术与科学电子出版社 / 2011-7 / 42.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (115, '伊利亚特', ' [古希腊] 荷马 / 陈中梅 ', '名著', '9781596671713', 0, 2, 1, 0, 0, 9, 100, '  Random House / 2006 年 10 月 03 日 / $ 75.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (116, '物种起源', ' [英] 达尔文 / 苗德岁 ', '名著', '9784805315071', 0, 2, 1, 0, 0, 9, 97, '  四川人民出版社 / １９８３ / 2.3', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (117, '全本新注聊斋志异（全三册）', ' [清] 蒲松龄 著 / 朱其铠 等校注 ', '名著', '9781672288699', 0, 2, 1, 0, 0, 9, 20, '  江苏文艺出版社 / 2013-1 / 48.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (118, '自然哲学之数学原理', ' (英)牛顿 / 王克迪 ', '名著', '9781780601120', 0, 2, 1, 0, 0, 9, 238, '  Penguin Books / 1998-11-1 / $14.95(US) £8.99(UK) $21.99(CA)', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (119, '热爱生命', ' (美)杰克·伦敦著 / 姬旭升 ', '名著', '9780851984957', 0, 2, 1, 0, 0, 9, 48, '  上海书店出版社 / 2009年1月 / 800', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (120, '道连·葛雷的画像', ' [英] 奥斯卡·王尔德 / 荣如德 ', '名著', '9781786641564', 0, 2, 1, 0, 0, 9, 27, '  Basic Books / 2010-8-24 / USD 27.50', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (121, '包法利夫人', ' 【法】福楼拜 / 周克希 ', '名著', '9788377136836', 0, 2, 1, 0, 0, 9, 263, '  人民文学出版社 / 1997-12 / 9.20', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (122, '傲慢与偏见', ' [英] 简·奥斯丁 / 孙致礼 ', '名著', '9780275931681', 0, 2, 1, 0, 0, 9, 24, '  生活·读书·新知三联书店 / 2012-11 / 30.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (123, '押沙龙，押沙龙！', ' [美] 威廉·福克纳 / 李文俊 ', '名著', '9781285427348', 0, 2, 1, 0, 0, 9, 247, '  新世界出版社 / 2010-1 / 25.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (124, '飞鸟集', ' [印度] 泰戈尔 / 郑振铎 ', '名著', '9781428036314', 0, 2, 1, 0, 0, 9, 81, '  中国友谊出版公司 / 1984年 / 20(全套)', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (125, '百年孤独', ' （哥伦比亚）加西亚・马尔克斯 / 黄锦炎／等 ', '名著', '9781910949016', 0, 2, 1, 0, 0, 9, 141, '  Andre Deutsch / 2004-08-16 / GBP 6.99', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (126, '围城', ' 钱钟书 ', '名著', '9781937412012', 0, 2, 1, 0, 0, 9, 19, '  Bloomsbury USA / 2008-09-30 / USD 16.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (127, '小王子', ' 【法国】圣埃克苏佩里 / 林珍妮 / 马振骋 ', '名著', '9781878576187', 0, 2, 1, 0, 0, 9, 63, '  上海人民出版社 / 2009-04 / 120.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (128, '契科夫短篇小说精选', ' 契诃夫 / 梅春才 ', '名著', '9781939851024', 0, 2, 1, 0, 0, 9, 477, '  华艺出版社 / 2005-1 / 25.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (129, '中央 约翰，克里斯朵夫（上下）', ' 罗曼·罗兰 / 许渊冲 ', '名著', '9781761030642', 0, 2, 1, 0, 0, 9, 42, '  联经出版公司 / 1984-05-01 / NT$ 2000', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (130, '野性的呼唤', ' [美]杰克·伦敦 ', '名著', '9780972860321', 0, 2, 1, 0, 0, 9, 158, '  VINTAGE BOOKS / 2004 / 7.99$', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (131, '神曲', ' 但丁 / 王维克 ', '名著', '9781580089821', 0, 2, 1, 0, 0, 9, 20, '  2007/08/29', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (132, '新月集·飞鸟集', ' [印] 泰戈尔 / 郑振铎 ', '名著', '9780123486554', 0, 2, 1, 0, 0, 9, 139, '  上海书店出版社 / 2013-3 / 175.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (133, '围城', ' 钱锺书 ', '名著', '9780231164122', 0, 2, 1, 0, 0, 9, 113, ' 06/16 / £18.99', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (134, '基督山伯爵', ' 大仲马 / 周克希 / 韩沪麟 ', '名著', '9781633441941', 0, 2, 1, 0, 0, 9, 50, '  中国华侨出版社 / 1999年5月 / 28', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (135, '百年孤独', ' [哥伦比亚] 加西亚·马尔克斯 / 黄锦炎 / 沈国正 / 陈泉 ', '名著', '9780571278893', 0, 2, 1, 0, 0, 9, 30, '  法律出版社 / 2011-10 / 38.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (136, '悲惨世界（上中下）', ' [法] 雨果 / 李丹 / 方于 ', '名著', '9780415732086', 0, 2, 1, 0, 0, 9, 35, '  九州出版社 / 2012-8 / 22.50元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (137, '教父', ' [美]马里奥·普佐 / 周汉林 ', '名著', '9781539069492', 0, 2, 1, 0, 0, 9, 46, '  Riverhead Trade / 2003-11-04 / USD 19.95', '文学,化学,心理,童话,经典文学', '1');
INSERT INTO `booktb` VALUES (138, '中国古代文化常识', ' 王力 编 ', '名著', '9781656892812', 0, 2, 1, 0, 0, 9, 118, '  上海译文出版社 / 1998 / 17.5', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (139, '傲慢与偏见', ' 简·奥斯丁 / 王科一 ', '名著', '9781520355825', 0, 2, 1, 0, 0, 9, 57, '  電影雙周刊 / 2004-11-1 / NT$ 360', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (140, '格林童话全集', ' 格林兄弟 / 魏以新 ', '名著', '9780851983110', 0, 2, 1, 0, 0, 9, 53, '  岳麓书社 / 1992-12-1 / 9.90', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (141, '卡夫卡小说全集（全三册）', ' [奥] 卡夫卡 / 韩瑞祥 [等] ', '名著', '9781425816315', 0, 2, 1, 0, 0, 9, 27, '  HarperCollins Publishers Limited / 2006-08-01 / USD 35.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (142, '鼠疫', ' (法)阿尔贝·加缪 / 刘方 ', '名著', '9781687002167', 0, 2, 1, 0, 0, 9, 24, '  上海音乐出版社 / 2001-9-1 / 150.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (143, '追忆似水年华', ' [法] 普鲁斯特 / 周克希 ', '名著', '9780548607800', 0, 2, 1, 0, 0, 9, 33, '  军事科学出版社 / 1989年 / 7.80', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (144, '罪与罚', ' 陀思妥耶夫斯基 (Dostoevsky) ', '名著', '9781925106992', 0, 2, 1, 0, 0, 9, 100, ' 07/2007 / £7.99', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (145, '契诃夫小说选', ' (俄)契诃夫 / 汝龙 ', '名著', '9780813809908', 0, 2, 1, 0, 0, 9, 26, '  上海人民出版社 / 1983年8月 / 5.50', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (146, '荷马史诗·伊利亚特', ' 荷马 / 罗念生 ', '名著', '9780486433950', 0, 2, 1, 0, 0, 9, 27, ' 张澄基译注 / 上海佛教书局印行 / 1996', '文学,化学,心理,经典', '1');
INSERT INTO `booktb` VALUES (147, '道连·葛雷的画像', ' [英] 奥斯卡·王尔德 / 荣如德 ', '名著', '9781912759262', 0, 2, 1, 0, 0, 9, 23, '  陕西师范大学出版总社有限公司 / 2013-1 / 29.80元', '文学,化学,心理,经典', '1');
INSERT INTO `booktb` VALUES (148, '泰戈尔诗集', ' [印] 罗宾德拉纳特·泰戈尔 / 深幻 / 王立 ', '名著', '9780563362357', 0, 2, 1, 0, 0, 9, 73, '  Bantam Press / 2006-09-01 / USD 35.83', '文学,化学,心理,经典', '1');
INSERT INTO `booktb` VALUES (149, '莎乐美 道林・格雷的画像', ' 奥斯卡・王尔德 / 孙法理 ', '名著', '9780195149449', 0, 2, 1, 0, 0, 9, 21, '  清华大学出版社 / 2012-4 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (150, '第二十二条军规', ' [美] 约瑟夫·赫勒 / 南文 / 赵守垠 / 王德明 译 / 主万 校 ', '名著', '9781440500367', 0, 2, 1, 0, 0, 9, 48, '  上海译文出版社 / 2001-9 / 19.60元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (151, '奥狄浦斯王', ' [古希腊] 索福克勒斯 / 罗念生 ', '名著', '9781616598761', 0, 2, 1, 0, 0, 9, 46, '  三采文化出版事業有限公司 / 2009-2 / $ 26.90', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (152, '骆驼祥子', ' 老舍 ', '名著', '9781904943884', 0, 2, 1, 0, 0, 9, 19, '  东方出版中心 / 1999-1-1 / 31.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (153, '莎士比亚四大悲剧', ' 威廉·莎士比亚 / 孙大雨 ', '名著', '9780898156034', 0, 2, 1, 0, 0, 9, 30, '  岳麓书社 / 2010-12 / 14.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (154, '吉檀迦利', ' （印度）泰戈尔 著 / 冰心 ', '名著', '9781546302971', 0, 2, 1, 0, 0, 9, 263, '  社会科学文献出版社 / 2014-9-1 / 72.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (155, '杰克·伦敦小说选', ' [美] 杰克·伦敦 / 万紫，雨宁，胡春兰 ', '名著', '9780122839559', 0, 2, 1, 0, 0, 9, 11439, '  上海译文出版社 / 2009-10 / 32.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (156, '莎士比亚喜剧悲剧集', ' 莎士比亚 / 朱生豪 ', '名著', '9781089159445', 0, 2, 1, 0, 0, 9, 4738, '  广西师范大学出版社 / 2004-5 / 32.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (157, 'Wuthering Heights', ' Emily Bronte ', '名著', '9788380084995', 2, 2, 1, 0, 0, 9, 5912, '  北京十月文艺出版社 / 2008-4 / 29.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (158, '傲慢与偏见', ' 简·奥斯丁(Jane Austen) / 王科一 ', '名著', '9781847884916', 0, 2, 1, 0, 0, 9, 197, '  生活·读书·新知三联书店 / 2013-6 / 45.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (159, '乌合之众', ' 【法】古斯塔夫·勒庞 / 夏杨 ', '名著', '9780811801041', 0, 2, 1, 0, 0, 9, 3259, '  花城出版社 / 2004-11-03 / 20.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (160, '悲惨世界', ' 雨果 / 李玉民 ', '名著', '9780415471558', 0, 2, 1, 0, 0, 9, 451, '  Tarcher / 1990-9-1 / USD 14.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (161, '几何原本', ' 欧几里得 ', '名著', '9780802844378', 0, 2, 1, 0, 0, 9, 48, '  遠見天下文化出版股份有限公司 / 2014-7-25 / NT$450', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (162, '傲慢与偏见', ' [英] 奥斯丁 / 张玲 / 张扬 ', '名著', '9780874746457', 0, 2, 1, 0, 0, 9, 1548, '  Penguin Books / 1988-5-3 / USD 17.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (163, '呐喊', ' 鲁迅 ', '名著', '9781452883816', 0, 2, 1, 0, 0, 9, 75, '  新星出版社 / 2013-6 / 32.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (164, '阿特拉斯耸耸肩（上下）', ' 安·兰德 / 杨格 ', '名著', '9781733011006', 0, 2, 1, 0, 0, 9, 425, '  广西师范大学出版社 / 2013-1 / 39.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (165, '飞鸟集', ' [印] 罗宾德拉纳德·泰戈尔 / 徐翰林 ', '名著', '9781565450882', 0, 2, 1, 0, 0, 9, 1133, '  生活·读书·新知三联书店 / 1991-3 / 18.60元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (166, '荆棘鸟', ' 考琳•麦卡洛 (Colleen McCullough) / 曾胡 ', '名著', '9781801142731', 0, 2, 1, 0, 0, 9, 455, '  生活·读书·新知三联书店 / 2013-1 / 36.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (167, '一个陌生女人的来信', ' [奥]斯台芬·茨威格 / 张玉书 ', '名著', '9781934043363', 0, 2, 1, 0, 0, 9, 470, '  花城出版社 / 1998-1 / 23.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (168, '白痴', ' [俄]陀思妥耶夫斯基 / 荣如德 ', '名著', '9781441334152', 0, 2, 1, 0, 0, 9, 517, '  文汇出版社 / 2008-01-01 / 37.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (169, '局外人', ' (法)阿尔贝・加缪 / 郭宏安 ', '名著', '9781903001035', 0, 2, 1, 0, 0, 9, 172, '  生活·读书·新知三联书店 / 2013-11 / 43.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (170, '浮士德', ' 歌德 / 钱春绮 ', '名著', '9781250000101', 0, 2, 1, 0, 0, 9, 130, '  广西师范大学出版社 / 2013-9 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (171, '彷徨', ' 鲁迅 ', '名著', '9780451468000', 0, 2, 1, 0, 0, 9, 46, '  中国轻工业出版社 / 2013-2 / 40.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (172, '安娜·卡列尼娜', ' （俄）列夫·托尔斯泰 / 草婴 ', '名著', '9780960115242', 0, 2, 1, 0, 0, 9, 2371, '  生活·读书·新知三联 / 2006-4 / 20.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (173, '沙丘', ' [美] 弗兰克·赫伯特 / 顾备 ', '名著', '9780764305603', 0, 2, 1, 0, 0, 9, 417, '  Back Bay Books / 1994-4-1 / USD 19.99', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (174, '水浒传', ' 施耐庵 / 罗贯中 ', '名著', '9780764304422', 0, 2, 1, 0, 0, 9, 239, '  Beacon Press / 2006-6-1 / 60.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (175, '野性的呼唤', ' 杰克·伦敦 / 刘荣跃 ', '名著', '9780764322624', 0, 2, 1, 0, 0, 9, 270, '  生活·读书·新知三联书店 / 2010-01-13 / 80.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (176, '欧·亨利短篇小说选', ' [美] 欧·亨利(O’Henry) / 王永年 ', '童话', '9780578630779', 0, 2, 1, 0, 0, 9, 21, '  中华书局 / 2013-8-11 / 990.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (177, '霍乱时期的爱情', ' [哥] 加西亚·马尔克斯 / 纪明荟 ', '名著', '9781520236001', 0, 2, 1, 0, 0, 9, 43, '  时代文艺出版社 / 2014-7-1 / 28.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (178, '故事新编', ' 鲁迅 ', '名著', '9781608997930', 0, 2, 1, 0, 0, 9, 607, '  长江文艺出版社 / 2012-7 / 35.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (179, '维莱特', ' 夏洛蒂·勃朗特 / 吴钧陶 ', '名著', '9781481302630', 0, 2, 1, 0, 0, 9, 43, '  上海人民出版社 / 2010-12 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (180, '道连·格雷的画像', ' （爱）王尔德 / 黄源深 ', '名著', '9780982718414', 0, 2, 1, 0, 0, 9, 1541, '  生活·读书·新知三联书店 / 2006-4 / 22.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (181, '美妙的新世界', ' 阿道斯•伦纳德•赫胥黎 (Aldous Leonard Huxley) / 孙法理 ', '名著', '9780632056569', 0, 2, 1, 0, 0, 9, 148, '  山东科学技术出版社 / 2005-7 / 65.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (182, '喧哗与骚动', ' (美)威廉·福克纳 / 李文俊 ', '名著', '9780691103006', 0, 2, 1, 0, 0, 9, 21, '  商务印书馆 / 2010-11 / 134.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (183, '荷马史诗·奥德赛', ' [古希腊] 荷马 / 王焕生 ', '童话', '9780857476968', 0, 2, 1, 0, 0, 9, 88, '  北京出版社 / 1983-10 / 2.15元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (184, '秘密花园', ' (美国)F.H.伯内特 / 李文俊 ', '名著', '9780198416883', 0, 2, 1, 0, 0, 9, 56, '  河南大学出版社 / 2013-5 / 22.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (185, '水浒传', ' [明] 施耐庵 / 罗贯中 ', '名著', '9781635301625', 0, 2, 1, 0, 0, 9, 1614, '  生活·读书·新知三联书店 / 2006-4 / 22.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (186, '彼得·潘', ' [英] 詹姆斯·巴里 / 孙国双 图 / 艾柯 ', '名著', '9781523509799', 0, 2, 1, 0, 0, 9, 15, '  商务印书馆 / 2013-9-1 / 42.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (187, '格林童话', ' 格林兄弟 / 施种 ', '童话', '9781643328348', 0, 2, 1, 0, 0, 9, 133, '  文汇出版社 / 2011-8 / 35.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (188, '小公主', ' (美)伯内特 ', '名著', '9781405922364', 0, 2, 1, 0, 0, 9, 31, '  赋格 / 2014-3-31 / 50元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (189, '呼啸山庄', ' (英) 艾米莉·勃朗特 / 杨苡 ', '名著', '9781910751343', 0, 2, 1, 0, 0, 9, 30, '  中国友谊出版公司 / 1986-12 / 3.20', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (190, '哈姆雷特', ' 莎士比亚 / 朱生豪 ', '名著', '9781879360112', 0, 2, 1, 0, 0, 9, 57, '  华东师范大学出版社 / 2011-7 / 580.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (191, '政治学', ' [古希腊] 亚里士多德 / 吴寿彭 ', '名著', '9781875093656', 0, 2, 1, 0, 0, 9, 122, '  宗教文化出版社 / 2003-12-1 / 20.0', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (192, '荆棘鸟', ' 考琳·麦卡洛 / 曾胡 ', '名著', '9781875582785', 0, 2, 1, 0, 0, 9, 69, '  中华书局 / 2000 / 19.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (193, '伤逝', ' 鲁迅 ', '童话', '9781875582310', 0, 2, 1, 0, 0, 9, 83, '  广西师范大学出版社 / 2007-5 / 32.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (194, '金瓶梅', ' 笑笑生 ', '名著', '9781840374391', 0, 2, 1, 0, 0, 9, 733, '  人民文学出版社 / 1997-11 / 78', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (195, '人类群星闪耀时', ' [奥]斯蒂芬·茨威格 / 彭浩容 ', '名著', '9781445600208', 0, 2, 1, 0, 0, 9, 25, '  天下遠見出版股份有限公司 / 2011-8-31 / NT$330', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (196, '物种起源', ' [英] 达尔文著 / 舒德干 ', '名著', '9780811707732', 0, 2, 1, 0, 0, 9, 119, '  重庆出版社 / 1982 / 0.40', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (197, '论语', ' 张燕婴 ', '名著', '9780850457278', 0, 2, 1, 0, 0, 9, 162, '  上海古籍 / 1997-06-01 / 16  元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (198, '马丁·伊登', ' 杰克·伦敦 / 吴劳 ', '童话', '9780850457261', 0, 2, 1, 0, 0, 9, 466, '  Hyperion / 2008-4-8 / USD 21.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (199, '九三年', ' （法）雨果 / 郑永慧 ', '名著', '9781482841268', 0, 2, 1, 0, 0, 9, 38, '  上海远东出版社 / 2011-8 / 128.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (200, '法国中尉的女人', ' [英] 约翰·福尔斯 / 陈安全 ', '名著', '9781570670664', 0, 2, 1, 0, 0, 9, 89, '  河北教育 / 2007-11 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (201, '简爱', ' [英] 夏洛蒂·勃朗特 / 盛世教育西方名著翻译委员会 ', '童话', '9788461149599', 0, 2, 1, 0, 0, 9, 20, '  Grove Press / 2012-6 / USD 25.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (202, '被伤害与侮辱的人们', ' [俄]陀思妥耶夫斯基 / 娄自良 ', '名著', '9781939578143', 0, 2, 1, 0, 0, 9, 75, '  中国社会科学出版社 / 1989.5 / 3.80', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (203, '一个陌生女人的来信', ' [奥] 斯台芬·茨威格 / 张玉书 ', '名著', '9780776622101', 0, 2, 1, 0, 0, 9, 21, '  机械工业出版社 / 2011-6 / 58.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (204, '美丽新世界', ' [英]阿道司.赫胥黎 / 宋龙艺 ', '名著', '9781421415000', 0, 2, 1, 0, 0, 9, 76, '  安徽文艺出版社 / 2000-9 / 21.80', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (205, '了不起的盖茨比', ' [美] 斯科特·菲茨杰拉德 著 / 村上春树 导读 / 邓若虚 ', '名著', '9781938706011', 0, 2, 1, 0, 0, 9, 70, '  深圳报业集团出版社 / 2012-6 / 38.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (206, '君主论', ' [意]尼科洛·马基雅维里 / 潘汉典 ', '名著', '9781657315099', 0, 2, 1, 0, 0, 9, 52, '  上海文艺出版社 / 1988 / 3.50元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (207, '罪与罚', ' [俄] 陀思妥耶夫斯基 / 朱海观 / 王汶 ', '童话', '9780811837941', 0, 2, 1, 0, 0, 9, 437, '  天津人民出版社 / 2006-4-1 / 22.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (208, '约翰·克利斯朵夫', ' （法）罗曼·罗兰 / 傅雷 ', '童话', '9781475205657', 0, 2, 1, 0, 0, 9, 74, '  上海古籍出版社 / 2014-2 / 38.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (209, '喧哗与骚动', ' (美)威廉﹒福克纳 / 李文俊 ', '名著', '9781582703121', 0, 2, 1, 0, 0, 9, 29, '  浙江大学出版社 / 2014-10 / 38', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (210, '简爱', ' 夏洛蒂•勃朗特 (Charlotte Bronte) / 宋兆霖 ', '童话', '9781718060685', 0, 2, 1, 0, 0, 9, 37, '  上海译文出版社 / 1979-10 / 1.30元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (211, '聊斋志异', ' 蒲松龄 ', '名著', '9781681403939', 0, 2, 1, 0, 0, 9, 20, '  北京大学出版社 / 2013-9 / 99.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (212, '九三年', ' [法]雨果 / 叶尊 ', '名著', '9781786439789', 0, 2, 1, 0, 0, 9, 45, '  Bloomsbury USA / 2009-9-29 / USD 24.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (213, '契诃夫短篇小说选', ' 契诃夫 / 汝龙 ', '名著', '9781078486552', 0, 2, 1, 0, 0, 9, 72, '  民族出版社 / 2000-2 / 15.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (214, '西游记（全二册）', ' 吴承恩 / 黄肃秋 注释 ', '名著', '9781078214988', 0, 2, 1, 0, 0, 9, 33, '  愛米粒 / 2013-10 / NT360', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (215, '一个陌生女人的来信', ' [奥] 斯台芬·茨威格 / 张玉书 ', '名著', '9781073488674', 0, 2, 1, 0, 0, 9, 28, '  University of Nebraska Press / 1943 / 19.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (216, '米德尔马契（全二册）', ' 乔治 艾略特 / 项星耀 ', '名著', '9781904738824', 0, 2, 1, 0, 0, 9, 21, '  李根芳 / 行人出版社 / 2007', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (217, '巴黎圣母院', ' （法）雨果 / 陈敬容 ', '名著', '9780955543142', 0, 2, 1, 0, 0, 9, 24, '  天下文化 / Jan 30, 2008 / NT$250', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (218, '爱伦·坡短篇小说集', ' （美）爱伦・坡 / 陈良廷 ', '名著', '9789993274063', 0, 2, 1, 0, 0, 9, 128, '  上海人民美术出版社 / 1983 / 2.20', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (219, '神秘岛', ' (法)儒勒.凡尔纳 / 联星 ', '名著', '9781733554909', 0, 2, 1, 0, 0, 9, 63, '  吉林音像出版社 / 2006 / RMB20.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (220, '卡夫卡中短篇小说选', ' [奥] 卡夫卡 著 / 韩瑞祥 / 仝保民 选编 / 韩瑞祥 / 杨劲 / 谢莹莹 / 王炳钧 / 叶廷芳 / 任卫东 / 薛思亮 ', '心理', '9780595394463', 0, 2, 1, 0, 0, 9, 64, '  中国华侨出版社 / 2013-9-1 / 35.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (221, '简爱', ' [英] 夏洛蒂.勃朗特 / 吴钧燮 ', '心理', '9780595146178', 0, 2, 1, 0, 0, 9, 58, '  清華大學 / 20041201 / NT$ 500', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (222, '马丁·伊登', ' （美）杰克・伦敦 / 殷惟本 ', '名著', '9781656405661', 0, 2, 1, 0, 0, 9, 167, '  Hyperion New York / 2008 / 128.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (223, '包法利夫人', ' [法]福楼拜 / 周克希 ', '名著', '9788492616053', 0, 2, 1, 0, 0, 9, 61, '  Little, Brown and Company / 2008-6 / GBP 7.34', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (224, '罗生门', ' （日）芥川龙之介 / 楼适夷 / 文洁若 / 吕元明 ', '名著', '9783319897608', 0, 2, 1, 0, 0, 9, 50, '  Touchstone / 1986-10-15 / $17.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (225, '幻灭', ' (法)巴尔扎克 / 傅雷 ', '名著', '9781979107518', 0, 2, 1, 0, 0, 9, 26, '  Vintage / 1989-04-23 / USD 15.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (226, '美丽新世界 （精装插图典藏版）', ' 阿道司·赫胥黎 (Aldous Huxley) / 李黎 / 薛人望 ', '心理', '9788366117624', 0, 2, 1, 0, 0, 9, 127, ' 5/25 / ¥2,310', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (227, '边城', ' 沈从文 ', '名著', '9781792931970', 0, 2, 1, 0, 0, 9, 95, '  生活·读书·新知三联书店 / 2009-9 / 20.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (228, '变形记', ' （古罗马）奥维德 / 杨周翰 ', '名著', '9780857232786', 0, 2, 1, 0, 0, 9, 43, '  中华书局 / 2002-8 / 36.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (229, '唐璜（上下册）', ' 拜伦 / 查良铮 ', '名著', '9780415836517', 0, 2, 1, 0, 0, 9, 79, '  人民文学出版社 / 1993-5 / 28.25元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (230, '尤利西斯', ' [爱尔兰] 詹姆斯·乔伊斯 / 金隄 ', '名著', '9780571323517', 0, 2, 1, 0, 0, 9, 23, '  Longman / 2000-01-01 / $7.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (231, '宽容', ' [美] 亨德里克·房龙 / 迮卫 / 靳翠微 ', '名著', '9781780895963', 0, 2, 1, 0, 0, 9, 36, '  华文出版社 / 2013-1 / 35.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (232, '家春秋（全3册）', ' 巴金 ', '心理', '9781925640915', 0, 2, 1, 0, 0, 9, 37, '  Modern Library / 12 June, 2001 / $14.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (233, '安娜·卡列宁娜（上下）', ' （俄）列夫・托尔斯泰 / 周扬，谢素台 ', '名著', '9780760348154', 0, 2, 1, 0, 0, 9, 63, '  吉林美术出版社 / 2010-1 / 138.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (234, '战争论（全三卷）', ' [德] 克劳塞维茨 / 中国人民解放军军事科学院 ', '心理', '9780815727422', 0, 2, 1, 0, 0, 9, 113, '  海南出版社 / 1998-6 / 24.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (235, '雪国 古都 千只鹤', ' [日] 川端康成 / 叶渭渠 / 唐月梅 ', '名著', '9780521032476', 0, 2, 1, 0, 0, 9, 26, '  明天出版社 / 2004-4-1 / 17.50', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (236, 'Jane Eyre', ' 夏洛蒂·勃朗特 ', '心理', '9781467136631', 2, 2, 1, 0, 0, 9, 64, '  HarperCollins UK / 2010-3-1 / USD 29.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (237, '边城', ' 沈从文 / 黄永玉 卓雅 插图. ', '名著', '9780452298651', 0, 2, 1, 0, 0, 9, 73, '  卓雅 选编、摄影 / 2010-4 / 260.00元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (238, '荆棘鸟', ' [澳] 考琳·麦卡洛 / 曾胡 ', '名著', '9780809149223', 0, 2, 1, 0, 0, 9, 137, '  江苏教育 / 2005-4 / 15.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (239, '罗生门', ' [日]芥川龙之介 / 林少华 ', '名著', '9781626982185', 0, 2, 1, 0, 0, 9, 46, '  Hyperion / 2004-10-06 / USD 24.95', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (240, '西方哲学史', ' 罗素 ', '名著', '9781722057626', 0, 2, 1, 0, 0, 9, 38, '  Harmony / 2009-10-13 / USD 25.00', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (241, '朝花夕拾', ' 鲁迅 ', '名著', '9781475852080', 0, 2, 1, 0, 0, 9, 24, '  講談社文庫 / 2010年4月 / 本体660円（税込）', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (242, '阿Q正传', ' 鲁迅 / 丰子恺 ', '名著', '9781250108821', 0, 2, 1, 0, 0, 9, 34, ' 祈竹仁宝哲', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (243, '追忆似水年华 Ⅰ', ' [法] M·普鲁斯特 / 李恒基 / 徐继曾 ', '名著', '9780451498731', 0, 2, 1, 0, 0, 9, 52, '  北京出版社 / 1990年8月第1版 / 7.30元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (244, '狂人日记', ' 鲁迅 ', '名著', '9781786817624', 0, 2, 1, 0, 0, 9, 85, '  哈尔滨出版社 / 2009-3 / 23.80元', '文学,化学,心理,童话,经典', '1');
INSERT INTO `booktb` VALUES (245, '日瓦戈医生', ' 〔苏〕鲍里斯·帕斯捷尔纳克 / 蓝英年 / 张秉衡 ', '名著', '9781542093385', 0, 2, 1, 0, 0, 9, 20, '  上海文艺出版社 / 1985 / 9.85', '文学', '1');
INSERT INTO `booktb` VALUES (246, '呼啸山庄', ' 艾米莉·勃朗特 / 方平 ', '文学', '9781524676902', 0, 2, 1, 0, 0, 9, 83, '  Pantheon / 2007-10 / 216.00元', '文学', '1');
INSERT INTO `booktb` VALUES (247, '麦琪的礼物', ' [美] 欧·亨利 / 张经浩 ', '名著', '9780996767712', 0, 2, 1, 0, 0, 9, 73, '  角川書店 / 2004 / 1,470', '文学', '1');
INSERT INTO `booktb` VALUES (248, '浮士德', ' 歌德 / 绿原 ', '文学', '9781542973366', 0, 2, 1, 0, 0, 9, 1813, '  上海人民出版社 / 2010-10-01 / 88.00', '文学', '1');
INSERT INTO `booktb` VALUES (249, '古都', ' 川端康成 / 唐月梅 ', '名著', '9781365866142', 0, 2, 1, 0, 0, 9, 2383, '  浙江大学出版社 / 2011-6 / 79.00元', '文学', '1');
INSERT INTO `booktb` VALUES (250, '呼啸山庄', ' [英] 艾米莉·勃朗特 / 杨苡 ', '文学', '9780809167814', 0, 2, 1, 0, 0, 9, 452, '  万卷出版公司出版 / 2010-11 / 48.00元', '文学', '1');
INSERT INTO `booktb` VALUES (251, '推销员之死', ' [美]阿瑟·米勒 / 英若诚 / 梅绍武 / 陈良廷 ', '文学', '9781601429179', 0, 2, 1, 0, 0, 9, 1121, '  南海出版公司 / 2010-8 / 36.00元', '文学', '1');
INSERT INTO `booktb` VALUES (252, '审判', ' [奥地利]弗朗茨﹒卡夫卡 / 冯亚琳 ', '文学', '9780262043403', 0, 2, 1, 0, 0, 9, 2862, '  华文出版社 / 2009-4 / 58.00', '文学', '1');
INSERT INTO `booktb` VALUES (253, '静静的顿河（全四册）', ' [苏] 肖洛霍夫 / 金人 ', '文学', '9780199216130', 0, 2, 1, 0, 0, 9, 513, '  生活·读书·新知三联书店 / 2013-1-1 / 39.00元', '文学', '1');
INSERT INTO `booktb` VALUES (254, '一千零一夜', ' 纳训 ', '文学', '9781316649718', 0, 2, 1, 0, 0, 9, 1455, '  上海译文出版社 / 2005-05-01 / 33.00', '文学', '1');
INSERT INTO `booktb` VALUES (255, '战争与和平（全四册）', ' [俄] 列夫·托尔斯泰 / 刘辽逸 ', '名著', '9783944312552', 0, 2, 1, 0, 0, 9, 1979, '  牛津大學出版社 / 2004-3-1 / HK$98', '文学', '1');
COMMIT;

-- ----------------------------
-- Table structure for booktype
-- ----------------------------
DROP TABLE IF EXISTS `booktype`;
CREATE TABLE `booktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `typename` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of booktype
-- ----------------------------
BEGIN;
INSERT INTO `booktype` VALUES (1, '名著');
INSERT INTO `booktype` VALUES (2, '文学');
INSERT INTO `booktype` VALUES (3, '心理');
INSERT INTO `booktype` VALUES (4, '童话');
COMMIT;

-- ----------------------------
-- Table structure for imgbean
-- ----------------------------
DROP TABLE IF EXISTS `imgbean`;
CREATE TABLE `imgbean` (
  `id` int(11) NOT NULL,
  `imgname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of imgbean
-- ----------------------------
BEGIN;
INSERT INTO `imgbean` VALUES (1, 'image1');
INSERT INTO `imgbean` VALUES (2, 'image2');
INSERT INTO `imgbean` VALUES (3, 'image3');
INSERT INTO `imgbean` VALUES (4, 'image4');
INSERT INTO `imgbean` VALUES (5, 'image5');
INSERT INTO `imgbean` VALUES (6, 'image6');
INSERT INTO `imgbean` VALUES (7, 'image7');
INSERT INTO `imgbean` VALUES (8, 'image8');
INSERT INTO `imgbean` VALUES (9, 'image9');
INSERT INTO `imgbean` VALUES (10, 'image10');
INSERT INTO `imgbean` VALUES (11, 'image11');
INSERT INTO `imgbean` VALUES (12, 'image12');
INSERT INTO `imgbean` VALUES (13, 'image13');
INSERT INTO `imgbean` VALUES (14, 'image14');
INSERT INTO `imgbean` VALUES (15, 'image15');
INSERT INTO `imgbean` VALUES (16, 'image16');
INSERT INTO `imgbean` VALUES (17, 'image17');
INSERT INTO `imgbean` VALUES (18, 'image18');
INSERT INTO `imgbean` VALUES (19, 'image19');
INSERT INTO `imgbean` VALUES (20, 'image20');
INSERT INTO `imgbean` VALUES (21, 'image21');
INSERT INTO `imgbean` VALUES (22, 'image22');
INSERT INTO `imgbean` VALUES (23, 'image23');
INSERT INTO `imgbean` VALUES (24, 'image24');
INSERT INTO `imgbean` VALUES (25, 'image25');
INSERT INTO `imgbean` VALUES (26, 'image26');
INSERT INTO `imgbean` VALUES (27, 'image27');
INSERT INTO `imgbean` VALUES (28, 'image28');
INSERT INTO `imgbean` VALUES (29, 'image29');
INSERT INTO `imgbean` VALUES (30, 'image30');
INSERT INTO `imgbean` VALUES (31, 'image31');
INSERT INTO `imgbean` VALUES (32, 'image32');
INSERT INTO `imgbean` VALUES (33, 'image33');
INSERT INTO `imgbean` VALUES (34, 'image34');
INSERT INTO `imgbean` VALUES (35, 'image35');
INSERT INTO `imgbean` VALUES (36, 'image36');
INSERT INTO `imgbean` VALUES (37, 'image37');
INSERT INTO `imgbean` VALUES (38, 'image38');
COMMIT;

-- ----------------------------
-- Table structure for jilvtb
-- ----------------------------
DROP TABLE IF EXISTS `jilvtb`;
CREATE TABLE `jilvtb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `bookid` int(11) DEFAULT NULL,
  `begintime` int(11) DEFAULT '0',
  `endtime` int(11) DEFAULT '0',
  `timeslot` varchar(255) DEFAULT NULL,
  `bookname` varchar(255) DEFAULT NULL,
  `begindate` varchar(255) DEFAULT NULL,
  `booktype` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of jilvtb
-- ----------------------------
BEGIN;
INSERT INTO `jilvtb` VALUES (3, 3, 1, 1650403102, 1650403138, '凌晨', '1', '2022-4-20', '名著');
INSERT INTO `jilvtb` VALUES (4, 3, 1, 1650403214, 1650403380, '凌晨', '1', '2022-4-20', '名著');
INSERT INTO `jilvtb` VALUES (5, 3, 1, 1650403384, 1650405200, '凌晨', '1', '2022-4-20', '名著');
INSERT INTO `jilvtb` VALUES (6, 1, 101, 1650486872, 1650487240, '凌晨', '罪与罚', '2022-4-21', '童话');
INSERT INTO `jilvtb` VALUES (7, 1, 101, 1650486903, 1650489445, '凌晨', '罪与罚', '2022-4-21', '童话');
INSERT INTO `jilvtb` VALUES (8, 1, 137, 1650487192, 1650487243, '凌晨', '教父', '2022-4-21', '童话');
INSERT INTO `jilvtb` VALUES (9, 1, 101, 1650489322, 1650495618, '凌晨', '罪与罚', '2022-4-21', '童话');
INSERT INTO `jilvtb` VALUES (10, 1, 101, 1650494386, 1650518136, '凌晨', '罪与罚', '2022-4-21', '童话');
INSERT INTO `jilvtb` VALUES (11, 1, 137, 1650518089, 0, '中午', '教父', '2022-4-21', '心理');
INSERT INTO `jilvtb` VALUES (12, 1, 101, 1650518114, 0, '中午', '罪与罚', '2022-4-21', '心理');
INSERT INTO `jilvtb` VALUES (13, 1, 183, 1650518179, 0, '中午', '荷马史诗·奥德赛', '2022-4-21', '心理');
INSERT INTO `jilvtb` VALUES (14, 1, 102, 1650518272, 1650520486, '中午', '傲慢与偏见', '2022-4-21', '心理');
INSERT INTO `jilvtb` VALUES (15, 1, 102, 1650520489, 0, '中午', '傲慢与偏见', '2022-4-21', '心理');
COMMIT;

-- ----------------------------
-- Table structure for nrbean
-- ----------------------------
DROP TABLE IF EXISTS `nrbean`;
CREATE TABLE `nrbean` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `zhengwen` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `fabutime` varchar(255) DEFAULT NULL,
  `type` int(11) DEFAULT '0',
  `imgnamest` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `zan` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of nrbean
-- ----------------------------
BEGIN;
INSERT INTO `nrbean` VALUES (5, 1, '123', '123', '2022年04月21日 05:23:14', 0, ',image15,image16', '1', 1);
INSERT INTO `nrbean` VALUES (6, 1, '123', '123', '2022年04月21日 05:24:27', 1, NULL, NULL, 1);
INSERT INTO `nrbean` VALUES (7, 1, '寂寞', '123', '2022年04月21日 13:55:59', 0, ',image30,image31', '来来来', 0);
INSERT INTO `nrbean` VALUES (8, 1, '啦啦啦啦', '情侣空间', '2022年04月21日 13:56:34', 1, NULL, '来来来', 0);
COMMIT;

-- ----------------------------
-- Table structure for pingjia
-- ----------------------------
DROP TABLE IF EXISTS `pingjia`;
CREATE TABLE `pingjia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `bookid` int(11) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `timest` varchar(255) DEFAULT NULL,
  `neirong` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pingjia
-- ----------------------------
BEGIN;
INSERT INTO `pingjia` VALUES (1, 3, 1, '11', '2022年04月20日   06:13:33', '该喝喝');
INSERT INTO `pingjia` VALUES (2, 1, 137, '来来来', '2022年04月21日   06:39:53', '来来来');
INSERT INTO `pingjia` VALUES (3, 1, 137, '来来来', '2022年04月21日   06:40:16', '间距');
INSERT INTO `pingjia` VALUES (4, 1, 137, '来来来', '2022年04月21日   13:14:57', '5666');
INSERT INTO `pingjia` VALUES (5, 1, 137, '来来来', '2022年04月21日   13:15:53', '4556666');
INSERT INTO `pingjia` VALUES (6, 1, 102, '来来来', '2022年04月21日   13:16:57', '111');
COMMIT;

-- ----------------------------
-- Table structure for userBean
-- ----------------------------
DROP TABLE IF EXISTS `userBean`;
CREATE TABLE `userBean` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` varchar(255) DEFAULT NULL COMMENT '账号',
  `name` varchar(255) DEFAULT NULL COMMENT '名字',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `sex` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `foreignability` int(11) DEFAULT NULL,
  `literatureability` int(11) DEFAULT NULL,
  `viewability` int(11) DEFAULT NULL,
  `thinkingability` int(11) DEFAULT NULL,
  `happyability` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userBean
-- ----------------------------
BEGIN;
INSERT INTO `userBean` VALUES (1, '1', '来老两来', '1', '男', 'image38', '计算机,化学,心理,童话,经典文学', 1, 21, 11, 9, 9);
INSERT INTO `userBean` VALUES (3, '11', '11', '11', '11', 'image9', '小说,宗教,历史,心理,童话', 0, 0, 0, 0, 0);
INSERT INTO `userBean` VALUES (4, '22', '22', '22', '男', NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO `userBean` VALUES (5, '123', '来来来', '123', '男', NULL, '科幻,政治学,童话,物理,小说', 0, 0, 0, 0, 0);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
