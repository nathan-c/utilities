# (top left(x,y), bottom right(x,y))
this1 = ((1, 1), (4, 4))
that1 = ((2, 2), (5, 5))


class Rectangle:
    left = 0
    right = 0
    top = 0
    bottom = 0

    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def area(self):
        return (self.right - self.left) * (self.top - self.bottom)

    def __repr__(self):
        return str((self.left, self.right, self.top, self.bottom))


# x_overlap = max(0, min(x12, x22) - max(x11, x21))
# y_overlap = max(0, min(y12, y22) - max(y11, y21));

# x11 = this.left,
# y11 = this.top,
# x12 = this.right,
# y12 = this.bottom,
# x21 = that.left,
# y21 = that.top,
# x22 = that.right,
# y22 = that.bottom,


def overlap_area(this, that):
    x_overlap = max(0, min(this.right, that.right) - max(this.left, that.left))
    y_overlap = max(0, min(this.bottom, that.bottom) - max(this.top, that.top))
    return x_overlap * y_overlap


def exclude(this, that):
    overlap = overlap_area(this, that)
    if overlap == 0:
        return [this]
    if overlap == this.area:
        return []
    left_in = that.left < this.left < that.right
    right_in = that.left < this.right < that.right
    top_in = that.bottom < this.top < that.top
    bottom_in = that.bottom < this.bottom < that.top
    # does top left overlap
    top_left_overlaps = left_in and top_in
    # does top right overlap
    top_right_overlaps = right_in and top_in
    # does bottom left overlap
    bottom_left_overlaps = left_in and bottom_in
    # does bottom right overlap
    bottom_right_overlaps = right_in and bottom_in

    ret_val = []

    if top_left_overlaps:
        if top_right_overlaps:
            ret_val = [Rectangle(this.left, this.right, that.bottom, this.bottom)]
        if bottom_left_overlaps:
            ret_val = [Rectangle(that.right, this.right, this.top, this.bottom)]
        ret_val = [Rectangle(this.left, that.right, that.bottom, this.bottom),
                   Rectangle(that.right, this.right, this.top, this.bottom)]
    if top_right_overlaps:
        if bottom_right_overlaps:
            ret_val = [Rectangle(this.left, that.left, this.top, this.bottom)]
        ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
                   Rectangle(that.left, this.right, that.bottom, this.bottom)]
    if bottom_right_overlaps:
        if bottom_left_overlaps:
            ret_val = [Rectangle(this.left, this.right, this.top, that.top)]
        ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
                   Rectangle(that.left, this.right, this.top, that.top)]
    if bottom_left_overlaps:
        ret_val = [Rectangle(this.left, that.left, this.top, that.top),
                   Rectangle(that.right, this.right, this.top, this.bottom)]
    if left_in:
        if right_in:
            ret_val = [Rectangle(this.left, this.right, this.top, that.top),
                       Rectangle(this.left, this.right, that.bottom, this.top)]
        ret_val = [Rectangle(this.left, this.right, this.top, that.top),
                   Rectangle(that.right, this.right, that.top, that.bottom),
                   Rectangle(this.left, this.right, that.bottom, this.bottom)]
    if right_in:
        ret_val = [Rectangle(this.left, this.right, this.top, that.top),
                   Rectangle(this.left, that.left, that.top, that.bottom),
                   Rectangle(this.left, this.right, that.bottom, this.bottom)]
    if top_in:
        if bottom_in:
            ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
                       Rectangle(that.right, this.right, this.top, this.bottom)]
        ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
                   Rectangle(that.left, that.right, that.bottom, this.bottom),
                   Rectangle(that.right, this.right, this.top, this.bottom)]
    if bottom_in:
        ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
                   Rectangle(that.left, that.right, this.top, that.top),
                   Rectangle(that.right, this.right, this.top, this.bottom)]
    ret_val = [Rectangle(this.left, that.left, this.top, this.bottom),
               Rectangle(that.left, that.right, this.top, that.top),
               Rectangle(that.left, that.right, that.bottom, this.bottom),
               Rectangle(that.right, this.right, this.top, this.bottom)]

    return [s for s in ret_val if not s.area == 0]


tests = (Rectangle(1, 2, 1, 2), Rectangle(1, 2, 1, 2))
tests = (Rectangle(1, 2, 1, 3), Rectangle(1, 2, 1, 2))
print(exclude(*tests))
