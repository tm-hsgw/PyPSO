# PyPSO

Pythonによる粒子群最適化（Particle Swarm Optimization, PSO）の実装です

---

## クラス

### `Particle`

探索エージェントである粒子のクラスです。

- フィールド
    - `List<float> Velocity`  
    速度ベクトルを表します。所属する`Swarm`によって更新されます。

- プロパティ
    - `List<float> Position`  
    位置ベクトルを表します。

    - `List<float> PersonalBest`  
    この粒子が見つけたうちで最良の位置を表します。

    - `float Error`  
    現在位置の評価値を表します。

    - `float PersonalBestError`  
    `PersonalBest`の評価値を表します。

- メソッド
    - `void Move()`  
    現在の速度を用いて位置を更新します。所属する`Swarm`によって呼び出されます。


### `Swarm`

粒子群のクラスです。`Particle`のインスタンス群を保持します。

- フィールド
    - `private float __w`  
    粒子速度の更新における慣性の重みを表す定数です。初期値は`0.7`です。

    - `private float __cp`  
    粒子速度の更新における`PersonalBest`への引力の重みの最大値を表す定数です。初期値は1.4です。

    - `private float __cg`  
    粒子速度の更新における`GlobalBest`への引力の重みの最大値を表す定数です。初期値は1.4です。

- プロパティ
    - `List<float> GlobalBest`  
    この粒子群が見つけたうちで最良の位置を表します。

    - `float GlobalBestError`  
    `GlobalBest`の評価値を表します。

- メソッド
    - `void Move(int epoch)`  
    所属する各粒子について、速度を更新したのち`Move()`を呼び出します。

        引数  
        - `int epoch`  
        これまでに行われた更新回数の累計です。現段階で粒子の運動に影響しないデバッグ用の引数です。


