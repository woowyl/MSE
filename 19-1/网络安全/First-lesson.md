# 网络安全简介

## 教材推荐
1. 《密码编码学与网络安全》 - Stallings著  电子工业出版社
    - 密码学
    - 网络应用安全
    - 网络攻防
2. 《web安全、隐私和商务》 - Simoson、Gene 机械工业出版社
3. 《计算机网络安全技术教程》 - 谢冬青 冷健  机械工业出版社
4. 《现代密码学理论与实践》 - WENBO MAO 毛文波
5. 《Computer Securite: Art adn Science》 - Matt Bishop
    - 访问控制 Access Control
6. 《Write Secure Code》  - Michael Howard, David LeBlance
    - 代码安全
        - 主动
        - 被动

## 授课目标
- 密码学
- **Web应用功能安全**
- 前沿专题
- 网络安全

## 古典密码学

### 古代密码
    - 羊皮传书  (对称加密模型)
    - 藏头诗    （
    - Caesar Cipher  （对称加密模型）

### Symmetric Cipher Model （对称加密）
   
#### 五要素
    - 明文 P
    - 密文 C
    - 加密算法  E
    - 解密算法 D
    - 密钥 K

#### 描述
    - 秘密必须全寓于密钥
    - 秘密必须全寓于必要 不等于 算法公开
        - 算法公开 但是仍然可能无法猜到密码（漏洞），必须使用穷举法
    - Need Key Exchange,密钥交换是难题
    - 谁是我们的敌人，谁是我们的朋友，这是革命的首要问题

#### Cryptograhphy Catalog
 - The type of perations used for transfroming plaintext to cliphertext
    - substitution
    - trasposition
    - product
-  the number of the keys used
    - symmetric, single-key
    - Asymmetic, two-key or public-key encryption

- the way in which the plaintext is processed
    - Block
    - Stream

#### 如何设计好的密码
    - 密钥的数量长度
    - 提高单字母表密码安全性
        - “多”对一 playfaire 密钥矩阵 分组大小
        - 一对多  vigenere Cipher
            - 猜长度
            - autokey cipher 先用密钥解密 再用解密出的明文当密钥继续加密

#### 安全的分类
    - unconditional security
        无论如何也破解不了（理论上）
    - computational security
        收益和成本不成比例
    - unconditional security

